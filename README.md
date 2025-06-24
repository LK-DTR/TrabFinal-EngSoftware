# Sistema de Gerenciamento Acadêmico para Professores

Um dashboard moderno para gerenciamento de turmas, análise de desempenho de alunos e controle de atividades acadêmicas, desenvolvido com React e Vite.

## 🚀 Funcionalidades

- **Perfil do Professor**: Visualização de informações pessoais e cronograma de aulas
- **Análise de Alunos**: Visualização detalhada do desempenho individual dos estudantes
- **Análise de Turmas**: Gráficos e relatórios de desempenho geral das turmas
- **Gerenciamento de Provas**: Agendamento, edição e cancelamento de avaliações
- **Sistema de Avisos**: Cronograma de eventos e notificações importantes
- **Troca de Perfis**: Interface multi-usuário para diferentes professores

## 🛠️ Tecnologias Utilizadas

- **React** 19.1.0 - Biblioteca para construção da interface
- **React Router DOM** - Navegação entre páginas
- **Vite** - Build tool e servidor de desenvolvimento
- **CSS3** - Estilização com tema escuro moderno
- **ESLint** - Linting e qualidade de código

## 📁 Estrutura do Projeto

```# Simulador de Provas - Zé da Gota Solutions

Uma plataforma de estudos desenvolvida para ajudar estudantes do ensino fundamental e médio a se prepararem para provas, oferecendo simulados interativos e relatórios de desempenho detalhados. O projeto também fornece um dashboard para que professores possam acompanhar o progresso de suas turmas.

**Status do Projeto:** 🟢 Em Desenvolvimento - Sprint 2

---

## 🎯 Conceito do Projeto

O objetivo é criar uma solução para as principais dores de estudantes e professores no ensino básico. A plataforma busca oferecer um feedback de desempenho útil e direcionado para os alunos e, ao mesmo tempo, fornecer aos professores métricas consolidadas para identificar lacunas de aprendizagem e orientar suas aulas.

## ✨ Funcionalidades Planejadas

### Para Alunos
- [ ] Realizar Simulados por matéria.
- [ ] Visualizar relatório de desempenho detalhado após cada simulado.
- [ ] Receber recomendações de estudo personalizadas.

### Para Professores
- [ ] Acessar dashboard consolidado do desempenho da turma.
- [ ] Analisar as principais dificuldades dos alunos.

### Funcionalidades do Sistema
- [X] Cadastro e gerenciamento (CRUD) de questões de múltipla escolha.
- [ ] Correção automática dos simulados.

## 🛠️ Tecnologias Utilizadas

A arquitetura do projeto é dividida em back-end e front-end.

### Back-end
* **Python com FastAPI:** Para a construção da API REST.
* **SQLAlchemy:** ORM para comunicação com o banco de dados.
* **SQLite / PostgreSQL:** Banco de dados relacional.
* **Pytest:** Para testes automatizados da API.

### Front-end
* **React:** Biblioteca para construção da interface do usuário.
* **Vite:** Ferramenta de build e servidor de desenvolvimento.
* **Material-UI:** Biblioteca de componentes para a interface.
* **Axios:** Para realizar chamadas à API.

## 📁 Estrutura do Projeto
src/
├── components/          # Componentes reutilizáveis
│   ├── Calendario.jsx   # Cronograma e avisos
│   ├── ImageModal.jsx   # Modal para expansão de imagens
│   ├── ProfileSelector.jsx # Seletor de perfil ativo
│   └── Sidebar.jsx      # Menu de navegação lateral
├── pages/               # Páginas principais
│   ├── Perfil.jsx       # Página do perfil do professor
│   ├── AnaliseAlunos.jsx # Análise individual de alunos
│   ├── AnaliseTurma.jsx  # Análise geral das turmas
│   └── GerenciamentoProvas.jsx # Gerenciamento de provas
├── data/                # Dados JSON simulados
│   ├── alunos.json      # Dados dos estudantes
│   ├── professores.json # Dados dos professores
│   ├── turmas.json      # Informações das turmas
│   ├── provas.json      # Provas agendadas
│   ├── avisos.json      # Avisos e notificações
│   ├── imgs/            # Fotos de perfil
│   ├── analises/        # Gráficos de análise individual
│   └── analises_turmas/ # Gráficos de análise de turmas
└── App.jsx              # Componente principal
```

## 🚀 Como Executar

### Pré-requisitos
- Node.js (versão 16 ou superior)
- npm ou yarn

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/LK-DTR/TrabFinal-EngSoftware
cd TrabFinal-EngSoftware
```

2. Instale as dependências:
```bash
npm install
```

3. Execute o projeto em modo de desenvolvimento:
```bash
npm run dev
```

4. Acesse no navegador: `http://localhost:5173`

### Scripts Disponíveis

```bash
npm run dev     # Inicia o servidor de desenvolvimento
npm run build   # Gera build de produção
npm run lint    # Executa linting do código
npm run preview # Visualiza o build de produção
```

## 🎯 Funcionalidades Detalhadas

### Sistema de Perfis
- Troca dinâmica entre diferentes professores usando o [`ProfileSelector`](src/components/ProfileSelector.jsx)
- Dados persistentes por sessão através do estado do [`App.jsx`](src/App.jsx)

### Visualização de Dados
- **Fotos de perfil clicáveis**: Expansão em modal usando [`ImageModal`](src/components/ImageModal.jsx)
- **Gráficos de análise**: Visualização de desempenho individual e por turma
- **Cronograma dinâmico**: Exibição automática de horários e avisos no [`Calendario`](src/components/Calendario.jsx)

### Gerenciamento de Provas
- Agendamento de novas avaliações
- Edição de provas existentes
- Sistema de cancelamento com confirmação
- Interface formulário dinâmica

## 📊 Estrutura de Dados

### Professores ([professores.json](src/data/professores.json))
```json
{
  "id": 1,
  "nome": "Nome do Professor",
  "email": "email@utfpr.edu.br",
  "foto_perfil": "foto.png",
  "turmas_ids": [101, 102]
}
```

### Turmas ([turmas.json](src/data/turmas.json))
```json
{
  "id": 101,
  "nome": "Engenharia de Software",
  "curso": "Engenharia da Computação",
  "periodo": "6º Período",
  "horarios": [...],
  "analise_geral": "turma-101-analise.png",
  "aluno_ids": [201, 202, 205]
}
```

## 🎨 Design e Interface

- **Tema escuro moderno** com cores principais: `#242424`, `#ffea00`, `#646cff`
- **Layout responsivo** com sidebar fixa e conteúdo scrollável
- **Componentes interativos** com hover effects e transições suaves
- **Tipografia otimizada** para legibilidade em telas

## 🔧 Configuração de Desenvolvimento

O projeto utiliza:
- **Vite** para build rápido e HMR
- **ESLint** com configurações para React
- **CSS Modules** para estilização isolada
- **React Router** para navegação SPA

## 📝 Próximos Passos

- [ ] Infraestrutura
- [ ] Testes Aturomatizados

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.