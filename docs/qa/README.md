# 📋 Documentação de QA - Simulador de Provas

Esta pasta contém toda a documentação relacionada à **Qualidade e Testes** do projeto Simulador de Provas.

## 📄 Arquivos Disponíveis

### 🧪 [plano-de-testes.md](./plano-de-testes.md)
**Versão:** 1.1 | **Última atualização:** Julho 2025

Documento completo que define a estratégia de testes para o projeto, incluindo:

- **27 casos de teste** organizados por módulo
- **8 categorias** de funcionalidades cobertas
- **Matriz de rastreabilidade** ligando testes às histórias de usuário
- **Critérios de aceitação** e métricas de qualidade
- **Estratégia de execução** em 3 fases

#### Cobertura de Testes:
- ✅ Autenticação e Autorização (CT001-CT003)
- ✅ Funcionalidades do Aluno (CT004-CT007)
- ✅ Relatórios de Desempenho (CT008-CT010)
- ✅ Dashboard do Professor (CT011-CT013)
- ✅ Gerenciamento de Questões + API ENEM (CT014-CT018)
- ✅ Performance (CT019-CT022)
- ✅ Responsividade (CT023-CT024)
- ✅ Segurança (CT025-CT027)

### 🐛 [template-bug-report.md](./template-bug-report.md)
**Última atualização:** Julho 2025

Template padronizado para reporte de bugs, incluindo:

- **Classificação** de severidade e prioridade
- **Seções organizadas** para informações técnicas
- **Campos específicos** para API externa (ENEM)
- **Rastreabilidade** com casos de teste
- **Critérios de resolução** claros

#### Uso do Template:
1. Copie o template para um novo arquivo
2. Preencha todas as seções aplicáveis
3. Anexe evidências (screenshots, logs)
4. Categorize adequadamente a severidade
5. Atribua para o desenvolvedor responsável

## 🎯 Objetivos da Documentação QA

### Para Testadores
- **Padronização** de processos de teste
- **Cobertura completa** das funcionalidades
- **Rastreabilidade** de defeitos
- **Métricas** de qualidade

### Para Desenvolvedores
- **Critérios de aceitação** claros
- **Casos de teste** para validação
- **Processo estruturado** de correção de bugs
- **Definição de pronto**

### Para o Projeto
- **Qualidade garantida** em todas as entregas
- **Documentação** de evidências de teste
- **Processo** repetível e escalável
- **Comunicação** eficiente entre equipes

## 📊 Métricas de Qualidade Definidas

### Critérios de Aprovação
- ✅ **100%** dos casos de teste de prioridade Alta devem passar
- ✅ **90%** dos casos de teste de prioridade Média devem passar
- ✅ **0** bugs críticos ou bloqueadores
- ✅ Máximo **3** bugs menores aceitáveis

### Critérios de Performance
- ⚡ Carregamento inicial: **< 3 segundos**
- ⚡ Geração de relatórios: **< 3 segundos**
- ⚡ Correção automática: **< 1 segundo**
- ⚡ API externa (ENEM): **< 10 segundos**

## 🔄 Processo de Testes

### Fase 1: Testes Críticos
- Autenticação e autorização
- Fluxo principal dos simulados
- Geração de relatórios
- Dashboard do professor

### Fase 2: Testes Complementares
- CRUD de questões + API ENEM
- Responsividade
- Casos de borda

### Fase 3: Validação Final
- Performance completa
- Segurança e proteção
- Integração end-to-end

## 🚀 Como Usar Esta Documentação

### Para Executar Testes
1. Consulte o **plano-de-testes.md** para casos específicos
2. Execute os testes seguindo a ordem de prioridade
3. Documente resultados conforme critérios definidos
4. Use o template de bug para reportar problemas

### Para Reportar Bugs
1. Use o **template-bug-report.md** como base
2. Preencha todas as seções relevantes
3. Classifique adequadamente severidade/prioridade
4. Anexe evidências necessárias
5. Acompanhe o processo de resolução

---

**Responsável QA:** Lucas Cordeiro Dutra  
**Projeto:** Simulador de Provas - Zé da Gota Solutions  
**Última atualização:** Julho 2025
