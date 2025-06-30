from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
import httpx

from .. import crud, schemas, models
from ..database import get_db
from .auth import get_current_active_professor

router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)

# --- FUNÇÃO ADAPTADORA ---
# Responsável por converter o formato da questão do ENEM para o nosso formato interno
def map_enem_question_to_internal_schema(enem_question: schemas.ExternalQuestion) -> schemas.QuestionCreate:
    # Cria o dicionário de opções no formato {"A": "Texto da A", "B": "Texto da B", ...}
    options_dict = {alt.letter: alt.text for alt in enem_question.alternatives if alt.text}

    return schemas.QuestionCreate(
        question_text=enem_question.context,
        options=options_dict,
        correct_answer=enem_question.correctAlternative,
        subject=enem_question.discipline.capitalize()
    )


@router.post("/", response_model=schemas.Question, status_code=201)
def create_new_question(
    question: schemas.QuestionCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_professor)
):
    """
    Cria uma nova questão. Apenas usuários com a role 'professor' podem acessar este endpoint.
    """
    return crud.create_question(db=db, question=question)


# --- ROTA MODIFICADA ---
@router.get("/external/search/{year}", response_model=List[schemas.QuestionCreate])
async def search_external_questions(
    year: int,
    discipline: Optional[str] = None,
    limit: int = Query(10, ge=1, le=100) # Limite padrão de 10, máximo de 100
):
    """
    Busca questões na API pública do ENEM para um ano específico e as converte
    para o formato interno da nossa aplicação.
    """
    API_URL = f"https://api.enem.dev/v1/exams/{year}/questions"
    params = {"limit": 180} # A prova tem 180 questões, vamos buscar todas

    try:
        # Usamos 'async with' para gerenciar o ciclo de vida do cliente HTTP
        async with httpx.AsyncClient() as client:
            response = await client.get(API_URL, params=params, timeout=30.0)
            
            # Lança uma exceção para respostas com erro (4xx ou 5xx)
            response.raise_for_status()

            # Valida a resposta da API usando nosso schema Pydantic
            validated_data = schemas.EnemApiResponse.parse_obj(response.json())
            
            # Mapeia cada questão recebida para o nosso formato interno
            mapped_questions = [
                map_enem_question_to_internal_schema(q) 
                for q in validated_data.questions
            ]

            # Filtra pela disciplina, se o parâmetro foi fornecido
            if discipline:
                filtered_questions = [
                    q for q in mapped_questions 
                    if q.subject.lower() == discipline.lower()
                ]
            else:
                filtered_questions = mapped_questions
            
            # Retorna apenas a quantidade definida pelo parâmetro 'limit'
            return filtered_questions[:limit]

    except httpx.RequestError as exc:
        # Captura erros de conexão, timeout, etc.
        raise HTTPException(
            status_code=503, 
            detail=f"Erro ao se comunicar com a API do ENEM: {exc}"
        )
    except Exception as e:
        # Captura outros erros, como falha na validação do Pydantic
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro interno: {e}")