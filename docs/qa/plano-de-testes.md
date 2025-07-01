# 📋 Plano de Testes - Simulador de Provas
**Versão:** 1.1  
**Data:** Julho 2025  
**Responsável:** Lucas Cordeiro Dutra (QA)  

## 🎯 Objetivo
Este documento apresenta o plano de testes completo para garantir que todas as funcionalidades do Simulador de Provas atendam aos requisitos especificados e proporcionem uma experiência de usuário satisfatória.

## 📊 Escopo de Testes

### 🔍 Histórias de Usuário Cobertas
- **HU1:** Como aluno, quero realizar simulados por matéria para praticar meus conhecimentos
- **HU2:** Como aluno, quero visualizar relatório de desempenho detalhado após cada simulado
- **HU3:** Como professor, quero acessar dashboard consolidado do desempenho da turma

### 🛠️ Tipos de Teste
1. **Testes Funcionais**
2. **Testes de Interface de Usuário**
3. **Testes de API**
4. **Testes de Performance**
5. **Testes de Segurança**
6. **Testes de Responsividade**

## 🧪 Casos de Teste

### 1. Autenticação e Autorização

#### CT001 - Login de Aluno
**Descrição:** Verificar login de usuário aluno  
**Pré-condições:** Usuário aluno cadastrado no sistema  
**Passos:**
1. Acessar página de login
2. Inserir email válido de aluno
3. Inserir senha correta
4. Clicar em "Entrar"

**Resultado Esperado:** Redirecionamento para dashboard do aluno  
**Status:** ⏳ Pendente  

#### CT002 - Login de Professor
**Descrição:** Verificar login de usuário professor  
**Pré-condições:** Usuário professor cadastrado no sistema  
**Passos:**
1. Acessar página de login
2. Inserir email válido de professor
3. Inserir senha correta
4. Clicar em "Entrar"

**Resultado Esperado:** Redirecionamento para dashboard do professor  
**Status:** ⏳ Pendente  

#### CT003 - Login com Credenciais Inválidas
**Descrição:** Verificar comportamento com credenciais incorretas  
**Passos:**
1. Inserir email inválido ou senha incorreta
2. Tentar fazer login

**Resultado Esperado:** Mensagem de erro "Credenciais inválidas"  
**Status:** ⏳ Pendente  

### 2. Funcionalidades do Aluno (HU1)

#### CT004 - Seleção de Matéria para Simulado
**Descrição:** Verificar seleção de matéria no dashboard do aluno  
**Pré-condições:** Aluno logado no sistema  
**Passos:**
1. Acessar dashboard do aluno
2. Visualizar matérias disponíveis
3. Selecionar uma matéria específica

**Resultado Esperado:** Lista de simulados disponíveis para a matéria selecionada  
**Status:** ⏳ Pendente  

#### CT005 - Iniciar Simulado
**Descrição:** Verificar início de simulado  
**Pré-condições:** Matéria selecionada  
**Passos:**
1. Clicar em "Iniciar Simulado"
2. Confirmar início do teste

**Resultado Esperado:** Primeira questão do simulado exibida  
**Status:** ⏳ Pendente  

#### CT006 - Navegação entre Questões
**Descrição:** Verificar navegação durante o simulado  
**Pré-condições:** Simulado iniciado  
**Passos:**
1. Responder primeira questão
2. Clicar em "Próxima"
3. Verificar exibição da segunda questão
4. Clicar em "Anterior"
5. Verificar retorno à primeira questão

**Resultado Esperado:** Navegação fluida entre questões com respostas preservadas  
**Status:** ⏳ Pendente  

#### CT007 - Finalização de Simulado
**Descrição:** Verificar conclusão do simulado  
**Pré-condições:** Todas as questões respondidas  
**Passos:**
1. Responder todas as questões
2. Clicar em "Finalizar Simulado"
3. Confirmar finalização

**Resultado Esperado:** Redirecionamento para tela de resultados  
**Status:** ⏳ Pendente  

### 3. Relatórios de Desempenho (HU2)

#### CT008 - Visualização de Resultado Imediato
**Descrição:** Verificar exibição de resultado após simulado  
**Pré-condições:** Simulado finalizado  
**Passos:**
1. Finalizar simulado
2. Acessar tela de resultados

**Resultado Esperado:** 
- Percentual de acertos
- Número de questões corretas/incorretas
- Tempo total utilizado
**Status:** ⏳ Pendente  

#### CT009 - Detalhamento por Questão
**Descrição:** Verificar análise detalhada das respostas  
**Pré-condições:** Na tela de resultados  
**Passos:**
1. Clicar em "Ver Detalhes"
2. Analisar questão por questão

**Resultado Esperado:** 
- Resposta do aluno
- Resposta correta
- Explicação da questão
**Status:** ⏳ Pendente  

#### CT010 - Recomendações de Estudo
**Descrição:** Verificar geração de recomendações personalizadas  
**Pré-condições:** Resultado do simulado disponível  
**Passos:**
1. Acessar seção de recomendações
2. Verificar sugestões de estudo

**Resultado Esperado:** Lista personalizada de tópicos para estudo baseada no desempenho  
**Status:** ⏳ Pendente  

### 4. Dashboard do Professor (HU3)

#### CT011 - Visualização Geral da Turma
**Descrição:** Verificar dashboard do professor  
**Pré-condições:** Professor logado com turmas associadas  
**Passos:**
1. Acessar dashboard do professor
2. Selecionar uma turma
3. Visualizar métricas gerais

**Resultado Esperado:** 
- Média geral da turma
- Número de alunos que fizeram simulados
- Distribuição de notas
**Status:** ⏳ Pendente  

#### CT012 - Análise por Matéria
**Descrição:** Verificar análise específica por disciplina  
**Pré-condições:** No dashboard do professor  
**Passos:**
1. Selecionar matéria específica
2. Analisar desempenho da turma

**Resultado Esperado:** Estatísticas detalhadas por matéria com gráficos  
**Status:** ⏳ Pendente  

#### CT013 - Identificação de Dificuldades
**Descrição:** Verificar identificação de pontos fracos da turma  
**Pré-condições:** Dados de simulados disponíveis  
**Passos:**
1. Acessar seção "Principais Dificuldades"
2. Analisar tópicos com menor desempenho

**Resultado Esperado:** Lista ordenada dos tópicos com maior dificuldade  
**Status:** ⏳ Pendente  

### 5. Gerenciamento de Questões (Professor)

#### CT014 - Criação de Nova Questão
**Descrição:** Verificar adição de questão pelo professor  
**Pré-condições:** Professor logado  
**Passos:**
1. Acessar "Gerenciar Questões"
2. Clicar em "Nova Questão"
3. Preencher formulário completo
4. Salvar questão

**Resultado Esperado:** Questão criada e disponível na base de dados  
**Status:** ⏳ Pendente  

#### CT015 - Edição de Questão Existente
**Descrição:** Verificar modificação de questão  
**Pré-condições:** Questão existente criada pelo professor  
**Passos:**
1. Localizar questão na lista
2. Clicar em "Editar"
3. Modificar informações
4. Salvar alterações

**Resultado Esperado:** Questão atualizada com novas informações  
**Status:** ⏳ Pendente  

#### CT016 - Exclusão de Questão
**Descrição:** Verificar remoção de questão  
**Pré-condições:** Questão existente  
**Passos:**
1. Selecionar questão
2. Clicar em "Excluir"
3. Confirmar exclusão

**Resultado Esperado:** Questão removida do sistema  
**Status:** ⏳ Pendente  

#### CT017 - Importação de Questões do ENEM
**Descrição:** Verificar integração com API externa do ENEM  
**Pré-condições:** Professor logado, API do ENEM acessível  
**Passos:**
1. Acessar "Importar Questões"
2. Selecionar ano da prova (ex: 2022)
3. Escolher disciplina (opcional)
4. Definir limite de questões
5. Confirmar importação

**Resultado Esperado:** Questões do ENEM importadas e convertidas para formato interno  
**Status:** ⏳ Pendente  

#### CT018 - Validação de Questões Importadas
**Descrição:** Verificar integridade das questões importadas da API do ENEM  
**Pré-condições:** Questões importadas disponíveis  
**Passos:**
1. Visualizar questão importada
2. Verificar estrutura (enunciado, alternativas, resposta correta)
3. Conferir metadados (disciplina, ano)

**Resultado Esperado:** Questões com estrutura correta e dados precisos  
**Status:** ⏳ Pendente  

### 6. Testes de Performance

#### CT019 - Tempo de Carregamento do Dashboard
**Descrição:** Verificar performance do carregamento inicial  
**Critério:** Página deve carregar em até 3 segundos  
**Status:** ⏳ Pendente  

#### CT020 - Geração de Relatórios
**Descrição:** Verificar tempo de geração de relatórios  
**Critério:** Relatórios devem ser gerados em até 3 segundos  
**Status:** ⏳ Pendente  

#### CT021 - Correção Automática
**Descrição:** Verificar velocidade da correção de simulados  
**Critério:** Correção deve ser instantânea (< 1 segundo)  
**Status:** ⏳ Pendente  

#### CT022 - Performance da API Externa
**Descrição:** Verificar tempo de resposta da integração com API do ENEM  
**Critério:** Importação de questões deve ocorrer em até 10 segundos  
**Status:** ⏳ Pendente  

### 7. Testes de Responsividade

#### CT023 - Visualização em Mobile
**Descrição:** Verificar adaptação para dispositivos móveis  
**Passos:**
1. Acessar em smartphone (viewport 375px)
2. Testar todas as funcionalidades principais

**Resultado Esperado:** Interface adaptada e funcional em mobile  
**Status:** ⏳ Pendente  

#### CT024 - Visualização em Tablet
**Descrição:** Verificar adaptação para tablets  
**Passos:**
1. Acessar em tablet (viewport 768px)
2. Testar navegação e funcionalidades

**Resultado Esperado:** Layout otimizado para tablet  
**Status:** ⏳ Pendente  

### 8. Testes de Segurança

#### CT025 - Proteção de Rotas
**Descrição:** Verificar controle de acesso a páginas restritas  
**Passos:**
1. Tentar acessar dashboard sem login
2. Tentar acessar área de professor como aluno

**Resultado Esperado:** Redirecionamento para login ou erro de autorização  
**Status:** ⏳ Pendente  

#### CT026 - Validação de Dados
**Descrição:** Verificar sanitização de entradas  
**Passos:**
1. Inserir caracteres especiais em formulários
2. Tentar inserir scripts maliciosos

**Resultado Esperado:** Dados sanitizados e scripts bloqueados  
**Status:** ⏳ Pendente  

#### CT027 - Segurança da API Externa
**Descrição:** Verificar tratamento seguro de dados da API do ENEM  
**Passos:**
1. Monitorar requisições para api.enem.dev
2. Verificar validação de dados recebidos
3. Testar comportamento com respostas malformadas

**Resultado Esperado:** Dados validados e erros tratados adequadamente  
**Status:** ⏳ Pendente  

## 📋 Matriz de Rastreabilidade

| Caso de Teste | História de Usuário | Funcionalidade | Prioridade |
|---------------|-------------------|----------------|------------|
| CT001-CT003   | -                 | Autenticação   | Alta       |
| CT004-CT007   | HU1               | Simulados      | Alta       |
| CT008-CT010   | HU2               | Relatórios     | Alta       |
| CT011-CT013   | HU3               | Dashboard Prof | Alta       |
| CT014-CT018   | -                 | CRUD Questões + API ENEM | Alta |
| CT019-CT022   | -                 | Performance    | Alta       |
| CT023-CT024   | -                 | Responsividade | Média      |
| CT025-CT027   | -                 | Segurança      | Alta       |

## 🚀 Estratégia de Execução

### Fase 1: Testes Críticos (Prioridade Alta)
- Autenticação e autorização
- Fluxo principal dos simulados
- Geração de relatórios
- Dashboard do professor

### Fase 2: Testes Complementares (Prioridade Média)
- CRUD de questões
- Responsividade
- Casos de borda

### Fase 3: Testes de Validação Final
- Performance
- Segurança
- Integração completa

## 📊 Critérios de Aceitação

### Critérios de Aprovação
- ✅ 100% dos casos de teste de prioridade Alta devem passar
- ✅ 90% dos casos de teste de prioridade Média devem passar
- ✅ 0 bugs críticos ou bloqueadores
- ✅ Máximo 3 bugs menores aceitáveis

### Critérios de Performance
- ⚡ Carregamento inicial: < 3 segundos
- ⚡ Geração de relatórios: < 3 segundos
- ⚡ Correção automática: < 1 segundo

## 🐛 Gestão de Defeitos

### Classificação de Severidade
- **Crítico:** Sistema não funciona
- **Alto:** Funcionalidade principal comprometida
- **Médio:** Funcionalidade secundária afetada
- **Baixo:** Problema cosmético ou de usabilidade

### Processo de Reporte
1. Identificação do bug
2. Reprodução do problema
3. Documentação detalhada
4. Classificação de severidade
5. Atribuição para correção
6. Reteste após correção

## 📈 Métricas de Qualidade

### Indicadores de Acompanhamento
- **Taxa de Defeitos:** < 5 bugs por funcionalidade
- **Taxa de Retrabalho:** < 10%
- **Cobertura de Testes:** > 90% das funcionalidades
- **Tempo Médio de Correção:** < 2 dias para bugs críticos

---

**Nota:** Este plano será atualizado conforme o progresso do desenvolvimento e identificação de novos cenários de teste.
