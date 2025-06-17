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

```
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