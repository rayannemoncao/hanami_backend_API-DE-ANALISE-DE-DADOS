from fastapi import HTTPException, APIRouter, Query
import pandas as pd
from src.services.quantity_produtcs import quantity_of_products 
import os

RUNTIME_DIR = "src/runtime_data"
os.makedirs(RUNTIME_DIR, exist_ok=True)

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
def dados_dos_produtos(
    sort_by: str = Query(None, description= "Campo para ordenação: nome_produto, quantidade_vendida ou total_arrecadado"),
    ascending: bool = Query(False, description= "Ordenação crescente (True) ou decrescente (False)")
) -> dict:
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
        products_metrics = quantity_of_products(df, sort_by=sort_by, ascending=ascending)

        analytics = {
            "products_metrics": products_metrics,
        }
        return analytics
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar os dados: {str(e)}")