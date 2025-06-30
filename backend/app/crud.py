from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- CRUD de Usuário ---

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# --- CRUD de Questão ---

def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(**question.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def get_questions_by_subject(db: Session, subject: str, limit: int):
    return db.query(models.Question).filter(models.Question.subject == subject).limit(limit).all()

def get_question_by_id(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()


# --- CRUD de Simulado ---

def create_simulado(db: Session, user_id: int):
    db_simulado = models.Simulado(user_id=user_id)
    db.add(db_simulado)
    db.commit()
    db.refresh(db_simulado)
    return db_simulado

def get_simulado(db: Session, simulado_id: int):
    return db.query(models.Simulado).filter(models.Simulado.id == simulado_id).first()


def finalize_simulado(db: Session, simulado_id: int, score: float, answers: dict):
    # Atualiza o status do simulado
    db_simulado = get_simulado(db, simulado_id)
    if not db_simulado:
        return None
    db_simulado.status = "finalizado"
    
    # Cria o resultado
    db_resultado = models.Resultado(
        simulado_id=simulado_id,
        score=score,
        answers=answers
    )
    db.add(db_resultado)
    db.commit()
    db.refresh(db_simulado)
    return db_simulado

def get_resultado(db: Session, simulado_id: int):
    return db.query(models.Resultado).filter(models.Resultado.simulado_id == simulado_id).first()