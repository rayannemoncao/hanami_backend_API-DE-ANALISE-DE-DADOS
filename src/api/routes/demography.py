from fastapi import APIRouter, HTTPException
import os
import pandas as pd

from src.services.demography_and_region import (
    metrics_by_region,
    demographic_distribution
)

router = APIRouter(
    prefix="/demography",
    tags=["Demography"]
)

# ----------------------------------
# Pasta onde os arquivos são salvos
# ----------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RUNTIME_DIR = os.path.join(BASE_DIR, "..", "runtime_data")


def get_dataframe() -> pd.DataFrame:
    """
    Localiza o arquivo CSV ou XLSX mais recente
    e retorna um DataFrame.
    """
    if not os.path.exists(RUNTIME_DIR):
        raise HTTPException(
            status_code=404,
            detail="Pasta de dados não encontrada. Faça o upload primeiro."
        )

    arquivos = [
        os.path.join(RUNTIME_DIR, f)
        for f in os.listdir(RUNTIME_DIR)
        if f.endswith((".csv", ".xlsx"))
    ]

    if not arquivos:
        raise HTTPException(
            status_code=404,
            detail="Nenhum arquivo de dados encontrado. Faça o upload primeiro."
        )

    arquivo_mais_recente = max(arquivos, key=os.path.getctime)
    ext = os.path.splitext(arquivo_mais_recente)[1].lower()

    try:
        if ext == ".csv":
            return pd.read_csv(arquivo_mais_recente)
        elif ext == ".xlsx":
            return pd.read_excel(arquivo_mais_recente)
        else:
            raise HTTPException(
                status_code=415,
                detail="Tipo de arquivo não suportado."
            )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao carregar arquivo: {str(e)}"
        )


# =====================================================
# GET /demography/regional-performance
# =====================================================
@router.get("/regional-performance")
def regional_performance():
    """
    Retorna um JSON com cada região como chave
    e suas métricas como valor.
    """
    df = get_dataframe()
    return metrics_by_region(df)


# =====================================================
# GET /demography/customer-profile
# =====================================================
@router.get("/customer-profile")
def customer_profile():
    """
    Retorna distribuições demográficas
    Ex:
    {
        "genero": {"m": 60, "f": 40},
        "faixa_etaria": {...},
        "cidade": {...}
    }
    """
    df = get_dataframe()
    return demographic_distribution(df)
