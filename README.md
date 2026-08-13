# FinancasCrew — Back end / API

Este diretório contém a parte da API (back end) do projeto FinancasCrew.

Descrição simples:
- Esta pasta implementa a API/serviço que orquestra os agentes e tarefas do
  projeto FinancasCrew usando CrewAI. Aqui ficam o código que expõe a API,
  as configurações dos agentes e as rotinas responsáveis por gerar relatórios
  e dados financeiros.

Estrutura principal (resumida):
- `app.py`: ponto de entrada da API/serviço.
- `knowledge/financas_crew/`: implementação do `crew`, `main.py` e configs.
- `knowledge/financas_crew/config/agents.yaml`: definição dos agentes.
- `knowledge/financas_crew/config/tasks.yaml`: definição das tarefas.
- `src/` e `tools/`: código auxiliar e ferramentas personalizadas.

Como usar (rápido):
1. Defina variáveis de ambiente necessárias (ex.: `OPENAI_API_KEY`).
2. Instale dependências (use seu gerenciador preferido; projeto usa `pyproject.toml`).
3. Execute a API a partir desta pasta:

```powershell
python app.py
```

Observações:
- Configure `agents.yaml` e `tasks.yaml` para alterar comportamentos e saídas.
- Para desenvolvimento do CrewAI, comandos úteis incluem `crewai run` e `uv` (se
  estiver usando o fluxo recomendado pelo projeto).

Onde procurar mais:
- Código da crew: `knowledge/financas_crew/crew.py` e `knowledge/financas_crew/main.py`.
- Definições e exemplos: `knowledge/financas_crew/config/`.

Se quiser, posso também adicionar exemplos de endpoints, instruções de ambiente
ou um guia passo a passo para rodar localmente — quer que eu adicione isso?
