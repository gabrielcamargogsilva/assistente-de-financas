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

Ferramentas e Tecnologias:
- **Python**: Recomendado Python >= 3.10.
- **FastAPI**: framework web para construir a API (ASGI).
- **Uvicorn**: servidor ASGI leve para rodar a aplicação FastAPI.
- **CrewAI**: framework de agentes usado para orquestrar os agentes e tarefas.
- **Pydantic**: validação e parsing de modelos (usado com FastAPI/CrewAI).
- **UV**: gerenciador de dependências (projeto contém `pyproject.toml`).
- **Docker** (opcional): empacotamento e deploy em contêineres.
- **Git**: controle de versão.



## Acesse o projeto front end
- [FinancasCrew — Front end (GitHub)](https://github.com/gabrielcamargogsilva/assistente-de-financas-front-end.git)
- [FinancasCrew — Front end (deploy)](https://assistente-de-financas.vercel.app/)

## Autor 
 **Gabriel Camargo Gonçalves Silva**
 - [LinkedIn](https://www.linkedin.com/in/gabriel-camargo-dev/) | [Email](gabrielcamargogsilva@gmail.com)
 
## Licença
Este repositório (parte `back end`) está licenciado sob a Licença MIT — veja o arquivo [LICENSE](LICENSE) para os termos completos.