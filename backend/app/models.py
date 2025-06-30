from sqlalchemy import Column, Integer, String, Float, JSON, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False, default="aluno")  # "aluno" ou "professor"

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, nullable=False)
    options = Column(JSON, nullable=False)  # Ex: {"A": "Opção 1", "B": "Opção 2"}
    correct_answer = Column(String, nullable=False) # Ex: "A"
    subject = Column(String, index=True)

class Simulado(Base):
    __tablename__ = "simulados"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String, default="em_andamento") # "em_andamento", "finalizado"
    timestamp_inicio = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("User")
    resultado = relationship("Resultado", back_populates="simulado", uselist=False)

class Resultado(Base):
    __tablename__ = "resultados"
    
    id = Column(Integer, primary_key=True, index=True)
    simulado_id = Column(Integer, ForeignKey("simulados.id"))
    score = Column(Float, nullable=False)
    answers = Column(JSON, nullable=False) # Ex: {"question_id_1": "A", "question_id_2": "C"}
    timestamp_fim = Column(DateTime(timezone=True), default=func.now())

    simulado = relationship("Simulado", back_populates="resultado")