from pydantic import BaseModel, EmailStr
from typing import List, Dict, Any, Optional
from datetime import datetime

# --- Schemas de Questões ---

class QuestionBase(BaseModel):
    question_text: str
    options: Dict[str, str]
    correct_answer: str
    subject: str

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int

    class Config:
        orm_mode = True

# --- Schemas de Usuário ---

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    role: str = "aluno"

class User(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True

# --- Schemas de Simulado e Resultado ---

class SimuladoCreate(BaseModel):
    subject: str
    num_questions: int = 5 # Padrão de 5 questões por simulado

class Simulado(BaseModel):
    id: int
    user_id: int
    status: str
    timestamp_inicio: datetime
    
    class Config:
        orm_mode = True

class AnswerSubmit(BaseModel):
    answers: Dict[int, str] # {question_id: chosen_option_key}

class Resultado(BaseModel):
    id: int
    simulado_id: int
    score: float
    answers: Dict[int, str]
    timestamp_fim: datetime

    class Config:
        orm_mode = True

# --- Schemas de Autenticação ---

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

from typing import List, Optional

class ExternalAlternative(BaseModel):
    letter: str
    text: Optional[str] = None
    file: Optional[str] = None
    isCorrect: bool

class ExternalQuestion(BaseModel):
    title: str
    index: int
    discipline: str
    language: Optional[str] = None
    year: int
    context: str
    files: List[str] = []
    correctAlternative: str
    alternativesIntroduction: Optional[str] = None
    alternatives: List[ExternalAlternative]

class EnemApiResponse(BaseModel):
    questions: List[ExternalQuestion]