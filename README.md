# Simulador de Provas - Zé da Gota Solutions

Uma plataforma de estudos desenvolvida para ajudar estudantes do ensino fundamental e médio a se prepararem para provas, oferecendo simulados interativos e relatórios de desempenho detalhados. O projeto também fornece uma API robusta para gerenciamento de usuários, questões e resultados.

**Status do Projeto:** 🟢 Em Desenvolvimento - Sprint 2

---

## 🎯 Conceito do Projeto

O objetivo é criar uma solução completa para as principais dores de estudantes e professores no ensino básico. A plataforma oferece um feedback de desempenho útil e direcionado para os alunos e, ao mesmo tempo, fornece aos professores métricas consolidadas para identificar lacunas de aprendizagem e orientar suas aulas.

## ✨ Funcionalidades Implementadas

### Para Alunos
- ✅ Sistema de autenticação JWT
- ✅ Seleção e filtros de simulados por matéria, instituição e dificuldade
- ✅ Realização de simulados com cronômetro automático
- ✅ Navegação entre questões durante o simulado
- ✅ Correção automática e cálculo de pontuação
- ✅ Histórico detalhado de simulados realizados
- ✅ Relatórios de desempenho com estatísticas

### Para Professores
- ✅ Dashboard para acompanhamento de turmas
- ✅ Gerenciamento de questões (CRUD)
- ✅ Análise de desempenho por matéria
- 🔄 Dashboard consolidado do desempenho da turma

### Funcionalidades do Sistema
- ✅ API REST completa com FastAPI
- ✅ Autenticação e autorização JWT
- ✅ Banco de dados SQLite com SQLAlchemy
- ✅ Interface responsiva com Chakra UI
- ✅ Cronômetro com finalização automática
- ✅ Sistema de filtros avançados

## 🛠️ Tecnologias Utilizadas

### Backend
- **FastAPI** - Framework web moderno para Python
- **SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados relacional
- **JWT (python-jose)** - Autenticação segura
- **Passlib** - Hash de senhas
- **Pydantic** - Validação de dados
- **Uvicorn** - Servidor ASGI

### Frontend
- **React 18.3.1** - Biblioteca para construção da interface
- **Chakra UI** - Biblioteca de componentes
- **Framer Motion** - Animações e transições
- **Axios** - Cliente HTTP
- **Vite** - Build tool e servidor de desenvolvimento
- **ESLint** - Linting e qualidade de código

## 📁 Estrutura do Projeto
```
TrabFinal-EngSoftware/
├── backend/                          # API Backend (FastAPI)
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                   # Entrada principal da API
│   │   ├── database.py               # Configuração do banco de dados
│   │   ├── models.py                 # Modelos SQLAlchemy
│   │   ├── schemas.py                # Schemas Pydantic
│   │   ├── crud.py                   # Operações CRUD
│   │   └── routers/                  # Endpoints organizados por módulo
│   │       ├── auth.py               # Autenticação e autorização
│   │       ├── questions.py          # Gerenciamento de questões
│   │       └── simulados.py          # Simulados e resultados
│   ├── requirements.txt              # Dependências Python
│   ├── simulador.db                  # Banco de dados SQLite
│   └── README.md                     # Documentação do backend
├── simulador_provas/                 # Frontend React
│   ├── src/
│   │   ├── App.jsx                   # Componente principal
│   │   ├── main.jsx                  # Entrada da aplicação
│   │   ├── components/               # Componentes React
│   │   │   ├── LoginPage.jsx         # Página de login
│   │   │   ├── SimuladoSelectionPage.jsx # Seleção de simulados
│   │   │   ├── QuestionPage.jsx      # Interface do simulado
│   │   │   └── HistoryPage.jsx       # Histórico de simulados
│   │   ├── api/
│   │   │   └── mockapi.js            # API mock para desenvolvimento
│   │   └── assets/                   # Recursos estáticos
│   ├── package.json                  # Dependências Node.js
│   ├── vite.config.js               # Configuração do Vite
│   └── README.md                    # Documentação do frontend
├── docs/                            # Documentação do projeto
│   └── qa/
│       ├── plano-de-testes.md       # Plano de testes completo
│       └── template-bug-report.md   # Template para bugs
├── package.json                     # Configuração raiz
└── README.md                        # Este arquivo
```

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.9+ 
- Node.js 16+
- npm ou yarn

### 1. Configuração do Backend

```bash
# Navegue para a pasta do backend
cd backend

# Crie um ambiente virtual (recomendado)
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor da API
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

A API estará disponível em: `http://127.0.0.1:8000`
- Documentação automática: `http://127.0.0.1:8000/docs`

### 2. Configuração do Frontend

```bash
# Em um novo terminal, navegue para a pasta do frontend
cd simulador_provas

# Instale as dependências
npm install

# Execute o servidor de desenvolvimento
npm run dev
```

A aplicação estará disponível em: `http://localhost:5173`

### Scripts Disponíveis

#### Backend
```bash
uvicorn app.main:app --reload    # Servidor de desenvolvimento
python -m pytest                # Executar testes (quando implementados)
```

#### Frontend
```bash
npm run dev      # Servidor de desenvolvimento
npm run build    # Build de produção
npm run lint     # Linting do código
npm run preview  # Preview do build
```

## 🔌 API Endpoints

### Autenticação
- `POST /auth/token` - Login e geração de token JWT
- `POST /auth/register` - Registro de novos usuários

### Simulados
- `GET /simulados` - Listar simulados disponíveis
- `POST /simulados` - Criar novo simulado
- `POST /simulados/{id}/submit` - Enviar respostas
- `GET /simulados/{id}/result` - Obter resultado

### Questões
- `GET /questions` - Listar questões
- `POST /questions` - Criar nova questão
- `PUT /questions/{id}` - Atualizar questão
- `DELETE /questions/{id}` - Deletar questão

## 💾 Banco de Dados

### Modelos Principais

**User**
- id, email, hashed_password, role (aluno/professor)

**Question** 
- id, question_text, options (JSON), correct_answer, subject

**Simulado**
- id, user_id, status, timestamp_inicio

**Resultado**
- id, simulado_id, score, answers (JSON), timestamp_fim

## 🎨 Interface do Usuário

### Características do Design
- **Interface moderna** com Chakra UI
- **Tema azul corporativo** (`blue.800`, `blue.600`)
- **Layout responsivo** adaptável a mobile e desktop
- **Feedback visual** com toasts e loading states
- **Navegação intuitiva** com sidebar fixa

### Componentes Principais
- **LoginPage**: Autenticação com validação
- **SimuladoSelectionPage**: Lista e filtros de simulados
- **QuestionPage**: Interface do simulado com cronômetro
- **HistoryPage**: Histórico detalhado de resultados

## 🧪 Testes e Qualidade

O projeto inclui um plano de testes abrangente localizado em `docs/qa/plano-de-testes.md` que cobre:

### Tipos de Teste
- ✅ Testes Funcionais
- ✅ Testes de Interface de Usuário  
- ✅ Testes de API
- ✅ Testes de Performance
- ✅ Testes de Segurança
- ✅ Testes de Responsividade

### Histórias de Usuário Cobertas
- **HU1**: Como aluno, quero realizar simulados por matéria
- **HU2**: Como aluno, quero visualizar relatório de desempenho detalhado
- **HU3**: Como professor, quero acessar dashboard consolidado

### Critérios de Performance
- ⚡ Carregamento inicial: < 3 segundos
- ⚡ Geração de relatórios: < 3 segundos  
- ⚡ Correção automática: < 1 segundo

## 🔐 Segurança

- **Autenticação JWT** com tokens seguros
- **Hash de senhas** com bcrypt via Passlib
- **Validação de dados** com Pydantic
- **Proteção de rotas** no frontend e backend
- **CORS configurado** para desenvolvimento

## 📱 Funcionalidades Detalhadas

### Sistema de Simulados
- **Filtros avançados**: Por instituição, disciplina e dificuldade
- **Cronômetro inteligente**: Finalização automática quando o tempo acaba
- **Navegação livre**: Entre questões durante o simulado
- **Persistência**: Respostas salvas durante a navegação

### Relatórios de Desempenho
- **Estatísticas detalhadas**: Acertos, erros, tempo gasto
- **Histórico completo**: Todos os simulados realizados
- **Métricas visuais**: Pontuação e progresso

### Gerenciamento de Questões
- **CRUD completo**: Criar, listar, editar e deletar
- **Múltipla escolha**: Suporte a 5 alternativas por questão
- **Categorização**: Por matéria e dificuldade

## 🚧 Próximos Passos

### Sprint 3 - Funcionalidades Avançadas
- [ ] Dashboard completo do professor
- [ ] Relatórios gráficos com Chart.js
- [ ] Sistema de recomendações personalizadas
- [ ] Exportação de relatórios em PDF

### Sprint 4 - Qualidade e Deploy
- [ ] Testes automatizados com Jest/Pytest
- [ ] CI/CD com GitHub Actions
- [ ] Deploy em produção (Heroku/Vercel)
- [ ] Documentação completa da API

### Melhorias Futuras
- [ ] Integração com APIs externas de questões
- [ ] Sistema de notificações push
- [ ] Modo offline para simulados
- [ ] Análise de desempenho com IA

## 👥 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## � Suporte

Em caso de dúvidas ou problemas:
- Verifique a documentação em `backend/README.md`
- Consulte o plano de testes em `docs/qa/plano-de-testes.md`
- Use o template de bug em `docs/qa/template-bug-report.md`

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.