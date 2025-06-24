from fastapi import FastAPI
from .database import engine
from . import models
from .routers import questions

# Cria as tabelas no banco de dados (só na primeira vez)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inclui as rotas definidas no arquivo questions.py
app.include_router(questions.router)

@app.get("/")
def read_root():
    return {"Project": "Simulador de Provas - API"}