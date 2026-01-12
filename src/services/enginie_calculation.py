import pandas as pd

def calculate_financial_metrics(df: pd.DataFrame) -> dict[str, float]:
    receita_bruta = df["valor_final"].sum()  # soma de todas as vendas
    # usa .get para evitar erro se a coluna não existir
    deducoes = df["deducoes"].sum() if "deducoes" in df.columns else 0
    receita_liquida = receita_bruta - deducoes
    custo_produtos_vendidos = (df["preco_unitario"] * df["quantidade"]).sum()
    lucro_bruto = receita_liquida - custo_produtos_vendidos
    return {
        "receita_bruta": receita_bruta,
        "receita_liquida": receita_liquida,
        "lucro_bruto": lucro_bruto
    }

def calculate_sales_metrics(df: pd.DataFrame) -> dict[str, float]:
    total_vendas = df["id_transacao"].nunique() if "id_transacao" in df.columns else 0
    receita_bruta = df["valor_final"].sum()
    deducoes = df["deducoes"].sum() if "deducoes" in df.columns else 0
    receita_liquida = receita_bruta - deducoes
    ticket_medio = receita_liquida / total_vendas if total_vendas > 0 else 0
    return {
        "total_vendas": total_vendas,
        "ticket_medio": ticket_medio
    }