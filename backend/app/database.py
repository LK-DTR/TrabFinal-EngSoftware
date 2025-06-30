from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão para o banco de dados SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./simulador.db"

# O argumento connect_args={"check_same_thread": False} é necessário apenas para o SQLite
# para permitir que mais de um thread interaja com o banco de dados.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria uma fábrica de sessões (SessionLocal) que será usada para criar sessões de banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos declarativos do SQLAlchemy
Base = declarative_base()

# Função para obter uma sessão de banco de dados (Injeção de Dependência)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()