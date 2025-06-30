from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, schemas, models
from ..database import get_db
from .auth import get_current_active_professor

router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
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

@router.get("/external/search", response_model=List[schemas.Question])
def search_external_questions(subject: str = None, year: int = None):
    """
    Simula uma busca de questões em uma API externa, como a do ENEM.
    Retorna uma lista de questões mockadas.
    
    COMENTÁRIO DE IMPLEMENTAÇÃO REAL:
    Para uma chamada real, usaríamos uma biblioteca como a 'httpx'.
    O código seria algo como:
    
    import httpx
    
    async def search_real_api(subject: str, year: int):
        API_URL = "https://api.enem.gov.br/v1/questoes"
        params = {"subject": subject, "year": year}
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(API_URL, params=params)
                response.raise_for_status() # Lança exceção para erros HTTP
                return response.json()
            except httpx.RequestError as exc:
                raise HTTPException(status_code=503, detail=f"Erro ao contatar API externa: {exc}")
    
    # E então chamaríamos a função `search_real_api` aqui.
    """
    
    # Dados Mockados para simulação
    mocked_questions = [
        {
            "id": 901,
            "question_text": "Em uma reação de neutralização, qual produto é sempre formado além do sal?",
            "options": {"A": "Ácido", "B": "Base", "C": "Água", "D": "Óxido"},
            "correct_answer": "C",
            "subject": "Química"
        },
        {
            "id": 902,
            "question_text": "Qual o principal gás responsável pelo efeito estufa?",
            "options": {"A": "Oxigênio", "B": "Nitrogênio", "C": "Dióxido de Carbono", "D": "Hélio"},
            "correct_answer": "C",
            "subject": "Geografia"
        }
    ]
    
    if subject:
        return [q for q in mocked_questions if q['subject'].lower() == subject.lower()]
        
    return mocked_questions