# API - Simulador de Provas

Esta pasta contém o código-fonte do back-end para o projeto "Simulador de Provas". A API é responsável pelo gerenciamento de usuários (alunos e professores), questões, e pela lógica de criação e correção de simulados.

## Stack Tecnológica

* **Linguagem:** Python 3.9+
* **Framework:** FastAPI
* **Banco de Dados:** SQLite
* **ORM:** SQLAlchemy
* **Validação de Dados:** Pydantic
* **Autenticação:** JWT (JSON Web Tokens) com `passlib` para hashing de senhas.

## Configuração do Ambiente

Siga os passos abaixo para configurar e executar o projeto localmente.

### 1. Pré-requisitos

-   Python 3.9 ou superior instalado.
-   `pip` (gerenciador de pacotes do Python).

### 2. Instalação

Clone o repositório e navegue até a pasta do back-end:

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd TrabFinal-EngSoftware/backend
```

Crie um ambiente virtual (recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### 3. Executando a API

Com as dependências instaladas, inicie o servidor de desenvolvimento:

```bash
uvicorn app.main:app --reload
```

O servidor estará disponível em `http://127.0.0.1:8000`. O comando `--reload` faz com que o servidor reinicie automaticamente após qualquer alteração no código.

## Documentação Interativa da API

A API vem com uma documentação interativa gerada automaticamente. Após iniciar o servidor, acesse uma das URLs abaixo em seu navegador:

-   **Swagger UI:** `http://127.0.0.1:8000/docs`
    -   Permite visualizar e **testar cada endpoint** diretamente pelo navegador.
-   **ReDoc:** `http://127.0.0.1:8000/redoc`
    -   Oferece uma visualização mais limpa e hierárquica da documentação.

## Estrutura dos Endpoints

A API está dividida em três módulos principais.

---

### Módulo: Autenticação (`/auth`)

Responsável pelo registro de novos usuários e pela geração de tokens de acesso.

#### `POST /auth/register`

-   **Descrição:** Registra um novo usuário (aluno ou professor).
-   **Corpo da Requisição (`UserCreate`):**
    ```json
    {
      "email": "user@example.com",
      "password": "your_strong_password",
      "role": "aluno"
    }
    ```
-   **Resposta de Sucesso (200 OK):** `User` (sem a senha).

#### `POST /auth/token`

-   **Descrição:** Autentica um usuário e retorna um token JWT. A requisição deve ser feita no formato `application/x-www-form-urlencoded`.
-   **Corpo da Requisição (`OAuth2PasswordRequestForm`):**
    -   `username`: O e-mail do usuário.
    -   `password`: A senha do usuário.
-   **Resposta de Sucesso (200 OK):** `Token`.
    ```json
    {
      "access_token": "ey...",
      "token_type": "bearer"
    }
    ```

---

### Módulo: Questões (`/questions`)

Gerenciamento de questões dos simulados.

#### `POST /`

-   **Descrição:** Cria uma nova questão no banco de dados.
-   **Autenticação:** **Requerida**. Apenas usuários com `role` de **"professor"** podem acessar.
-   **Corpo da Requisição (`QuestionCreate`):**
    ```json
    {
      "question_text": "Qual a capital do Brasil?",
      "options": {
        "A": "Rio de Janeiro",
        "B": "São Paulo",
        "C": "Brasília"
      },
      "correct_answer": "C",
      "subject": "Geografia"
    }
    ```
-   **Resposta de Sucesso (201 Created):** `Question` (incluindo o ID da nova questão).

#### `GET /external/search`

-   **Descrição:** Simula uma busca por questões em uma fonte externa.
-   **Autenticação:** Não requerida.
-   **Query Params:**
    -   `subject` (string, opcional): Filtra por matéria.
    -   `year` (int, opcional): Filtra por ano (atualmente não implementado na lógica mockada).
-   **Resposta de Sucesso (200 OK):** Lista de `Question`.

---

### Módulo: Simulados (`/simulados`)

Endpoints para iniciar, responder e consultar simulados.

#### `POST /`

-   **Descrição:** Inicia um novo simulado para o usuário autenticado.
-   **Autenticação:** **Requerida**.
-   **Corpo da Requisição (`SimuladoCreate`):**
    ```json
    {
      "subject": "Geografia",
      "num_questions": 5
    }
    ```
-   **Resposta de Sucesso (201 Created):** Um objeto contendo os dados do simulado criado e a lista de questões (sem o campo `correct_answer`).

#### `POST /{simulado_id}/submit`

-   **Descrição:** Submete as respostas de um simulado em andamento. O sistema corrige as respostas, calcula o score e finaliza o simulado.
-   **Autenticação:** **Requerida**. O usuário deve ser o dono do simulado.
-   **Corpo da Requisição (`AnswerSubmit`):**
    ```json
    {
      "answers": {
        "1": "C",
        "2": "A",
        "5": "D"
      }
    }
    ```
-   **Resposta de Sucesso (200 OK):** `Resultado` (com o score e os detalhes da submissão).

#### `GET /{simulado_id}/result`

-   **Descrição:** Retorna o resultado detalhado de um simulado já finalizado.
-   **Autenticação:** **Requerida**. O usuário deve ser o dono do simulado.
-   **Resposta de Sucesso (200 OK):** `Resultado`.

## Estrutura de Pastas do Backend

A organização dos arquivos no diretório `app/` segue as melhores práticas para projetos FastAPI, separando as responsabilidades:

-   `main.py`: Ponto de entrada da aplicação. Inicializa o FastAPI e inclui os roteadores.
-   `database.py`: Configuração da conexão com o banco de dados (SQLAlchemy).
-   `models.py`: Definição das tabelas do banco de dados como classes Python (Modelos SQLAlchemy).
-   `schemas.py`: Definição dos formatos de dados para entrada e saída da API (Schemas Pydantic).
-   `crud.py`: Funções que realizam as operações no banco de dados (Create, Read, Update, Delete).
-   `routers/`: Diretório que contém os endpoints da API, divididos por módulo (`auth.py`, `questions.py`, etc.).