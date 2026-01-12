from fastapi import FastAPI, HTTPException, APIRouter
import pandas as pd
from src.services.enginie_calculation import (calculate_financial_metrics, calculate_sales_metrics)
import os

RUNTIME_DIR = "src/runtime_data"
os.makedirs(RUNTIME_DIR, exist_ok=True)

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/")
def dados_analiticos() -> dict:
    try:
        #lista os arquivo na pasta RUNTIME_DIR
        arquivos = [os.path.join(RUNTIME_DIR, f) for f in os.listdir(RUNTIME_DIR)]
        if not arquivos:
            raise HTTPException(status_code=404, detail="Nenhum arquivo de dados encontrado.")
        
        #carrega o arquivo de dados tratado mais recente
        arquivo_mais_recente = max(arquivos, key=os.path.getctime)
        ext = os.path.splitext(arquivo_mais_recente)[1].lower()
        if ext ==".csv":
            df = pd.read_csv(arquivo_mais_recente)
        elif ext ==".xlsx":
            df = pd.read_excel(arquivo_mais_recente)
        else:
            raise HTTPException(status_code=415, detail="Tipo de arquivo não suportado.")
        
        #calcula as métricas usando as funções do serviço
        financial_metrics = calculate_financial_metrics(df)
        sales_metrics = calculate_sales_metrics(df)

        analytics = {
            "financial_metrics": financial_metrics,
            "sales_metrics": sales_metrics
        }
        return analytics
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar os dados: {str(e)}")