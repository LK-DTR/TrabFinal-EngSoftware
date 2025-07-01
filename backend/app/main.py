from fastapi import FastAPI
from .database import engine, Base
from .routers import auth, questions, simulados
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:5173",  # A porta onde seu Front-end React está rodando
    "http://127.0.0.1:5173", # Outra forma de referenciar localhost na porta do Front-end
    # Adicione aqui qualquer outro domínio onde seu Front-end possa rodar em produção
    # "https://seu-dominio-frontend.com",
]

# Comando para criar as tabelas no banco de dados na inicialização
# Em um ambiente de produção, é mais comum usar ferramentas de migração como Alembic.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API - Simulador de Provas",
    description="API para gerenciar usuários, questões e simulados.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Lista de origens permitidas
    allow_credentials=True,      # Permitir cookies, cabeçalhos de autorização, etc.
    allow_methods=["*"],         # Permitir todos os métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],         # Permitir todos os cabeçalhos (incluindo Authorization)
)

# Inclusão dos roteadores dos módulos
app.include_router(auth.router)
app.include_router(questions.router)
app.include_router(simulados.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API do Simulador de Provas!"}