#!/usr/bin/env python
import sys
import warnings
from financas_crew.crew import FinancasCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Executa a tripulação de agentes para análise de gastos.
    """
    print("\n--- 💰 ASSISTENTE PESSOAL DE FINANÇAS 💰 ---")
    print("Cole abaixo a sua lista de gastos ou fatura (pressione Enter + Ctrl+D ou digite FIM em uma nova linha para encerrar):\n")
    
    # Captura múltiplas linhas de texto digitadas/coladas pelo usuário
    linhas = []
    while True:
        try:
            linha = input()
            if linha.strip().upper() == "FIM":
                break
            linhas.append(linha)
        except EOFError:
            break
            
    gastos_brutos = "\n".join(linhas)

    if not gastos_brutos.strip():
        print("Nenhum gasto informado. Encerrando execução.")
        return

    inputs = {
        'gastos_brutos': gastos_brutos
    }

    try:
        FinancasCrew().crew().kickoff(inputs=inputs)
        print("\n✅ Análise concluída com sucesso! O relatório foi salvo em 'relatorio_financeiro.md'.")
    except Exception as e:
        raise Exception(f"Ocorreu um erro ao executar a análise: {e}")

if __name__ == "__main__":
    run()