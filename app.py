# backend/app.py
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()

# Adiciona a pasta 'knowledge' ao sys.path
knowledge_path = str(Path(__file__).parent / "knowledge")
if knowledge_path not in sys.path:
    sys.path.insert(0, knowledge_path)

from financas_crew.crew import FinancasCrew

app = FastAPI(title="Assistente de Finanças AI API")

# Leitura dinâmica e conversão para LISTA a partir do .env
frontend_env = os.getenv("URL_FRONTEND", "")
# Separa por vírgula se houver mais de uma URL e remove espaços/barras no final
origins = [url.strip().rstrip("/") for url in frontend_env.split(",") if url.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Passa estritamente a lista gerada do .env
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GastosRequest(BaseModel):
    gastos_brutos: str

@app.post("/api/analisar-gastos")
async def analisar_gastos(request: GastosRequest):
    if not request.gastos_brutos.strip():
        raise HTTPException(status_code=400, detail="Envie ao menos um gasto para análise.")

    inputs = {
        'gastos_brutos': request.gastos_brutos
    }

    try:
        resultado = await FinancasCrew().crew().kickoff_async(inputs=inputs)
        return {"sucesso": True, "relatorio": str(resultado)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar a análise: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)