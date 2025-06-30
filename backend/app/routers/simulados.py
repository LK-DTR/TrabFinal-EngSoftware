from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Dict

from .. import crud, schemas, models
from ..database import get_db
from .auth import get_current_user

router = APIRouter(
    prefix="/simulados",
    tags=["Simulados"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def start_new_simulado(
    config: schemas.SimuladoCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Inicia um novo simulado para o aluno logado.
    - Cria uma sessão de simulado no banco.
    - Seleciona questões aleatórias com base no tema.
    - Retorna os dados do simulado e a lista de questões.
    """
    questions = crud.get_questions_by_subject(db, subject=config.subject, limit=config.num_questions)
    if not questions or len(questions) < config.num_questions:
        raise HTTPException(status_code=404, detail=f"Não há questões suficientes de '{config.subject}' para iniciar o simulado.")

    simulado = crud.create_simulado(db=db, user_id=current_user.id)
    
    # Remove a resposta correta antes de enviar para o aluno
    questions_for_student = []
    for q in questions:
        question_data = schemas.Question.from_orm(q).dict()
        del question_data['correct_answer']
        questions_for_student.append(question_data)

    return {"simulado": schemas.Simulado.from_orm(simulado), "questions": questions_for_student}


@router.post("/{simulado_id}/submit", response_model=schemas.Resultado)
def submit_simulado(
    simulado_id: int,
    submission: schemas.AnswerSubmit,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Recebe as respostas do aluno, corrige a prova, calcula o score e finaliza o simulado.
    """
    db_simulado = crud.get_simulado(db, simulado_id)
    
    if not db_simulado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Simulado não encontrado.")
    if db_simulado.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Este simulado não pertence ao usuário atual.")
    if db_simulado.status == "finalizado":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Este simulado já foi finalizado.")

    # Lógica de Correção Automática
    correct_count = 0
    total_questions = len(submission.answers)

    for question_id, user_answer in submission.answers.items():
        question = crud.get_question_by_id(db, question_id=int(question_id))
        if question and question.correct_answer == user_answer:
            correct_count += 1
            
    # Cálculo do Score
    score = (correct_count / total_questions) * 100 if total_questions > 0 else 0
    
    crud.finalize_simulado(db, simulado_id, score, submission.answers)
    
    resultado = crud.get_resultado(db, simulado_id)
    if not resultado:
        # Fallback, embora não deva acontecer na lógica normal
        raise HTTPException(status_code=500, detail="Erro ao salvar o resultado.")

    return resultado


@router.get("/{simulado_id}/result", response_model=schemas.Resultado)
def get_simulado_result(
    simulado_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Retorna o resultado detalhado de um simulado finalizado.
    """
    db_simulado = crud.get_simulado(db, simulado_id)
    if not db_simulado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Simulado não encontrado.")
    if db_simulado.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acesso negado.")
    if db_simulado.status != "finalizado":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="O simulado ainda não foi finalizado.")

    resultado = crud.get_resultado(db, simulado_id)
    if not resultado:
        raise HTTPException(status_code=404, detail="Resultado não encontrado para este simulado.")
        
    return resultado