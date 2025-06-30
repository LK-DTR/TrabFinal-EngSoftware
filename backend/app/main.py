from fastapi import FastAPI
from .database import engine, Base
from .routers import auth, questions, simulados

# Comando para criar as tabelas no banco de dados na inicialização
# Em um ambiente de produção, é mais comum usar ferramentas de migração como Alembic.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API - Simulador de Provas",
    description="API para gerenciar usuários, questões e simulados.",
    version="1.0.0"
)

# Inclusão dos roteadores dos módulos
app.include_router(auth.router)
app.include_router(questions.router)
app.include_router(simulados.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API do Simulador de Provas!"}