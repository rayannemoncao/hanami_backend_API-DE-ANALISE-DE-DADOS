import pandas as pd

def quantity_of_products (df: pd.DataFrame, sort_by: None, ascending: bool = False) -> list[dict[str, int]]:
    #Agrupa por nome do produto
    grouped = df.groupby ("nome_produto").agg(
        quantidade_vendida = pd.NamedAgg(column = "quantidade", aggfunc="sum"),
        total_arrecadado = pd.NamedAgg(column = "valor_final", aggfunc ="sum")
    ).reset_index()

    #Se sort_by for informado, ordena
    if sort_by in ["quantidade_vendida", "total_arrecadado", "nome_produto"]:
        grouped = grouped.sort_values(by=sort_by, ascending=ascending)
        
    #Converte para lista
    result = grouped.to_dict(orient="records")
    return result
    