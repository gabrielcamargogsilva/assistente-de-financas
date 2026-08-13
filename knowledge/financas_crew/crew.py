from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent



@CrewBase
class FinancasCrew():
    """FinancasCrew crew para análise e otimização de gastos"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def categorizador_financeiro(self) -> Agent:
        return Agent(
            config=self.agents_config['categorizador_financeiro'],
            verbose=True
        )

    @agent
    def analista_orcamento(self) -> Agent:
        return Agent(
            config=self.agents_config['analista_orcamento'],
            verbose=True
        )

    @agent
    def consultor_economia(self) -> Agent:
        return Agent(
            config=self.agents_config['consultor_economia'],
            verbose=True
        )

    @task
    def tarefa_categorizacao(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_categorizacao']
        )

    @task
    def tarefa_analise_orcamento(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_analise_orcamento']
        )

    @task
    def tarefa_plano_economia(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_plano_economia'],
            output_file='relatorio_financeiro.md'  # Salva o relatório final direto em Markdown!
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )