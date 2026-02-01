import pandas as pd


def metrics_by_region(df: pd.DataFrame) -> dict:
    """
    Agrupa dados por região e calcula métricas de vendas.
    Retorna um dicionário com a região como chave e suas métricas como valor.
    """

    grouped = (
        df.groupby("regiao")
        .agg(
            total_vendas=("valor_final", "sum"),
            quantidade_transacoes=("id_transacao", "count"),
            ticket_medio=("valor_final", "mean")
        )
        .round(2)
    )

    # Converte o DataFrame para dict no formato:
    # { "norte": {...}, "sul": {...} }
    return grouped.to_dict(orient="index")


def demographic_distribution(df: pd.DataFrame) -> dict:
    """
    Calcula a distribuição demográfica de clientes.
    Retorna percentuais por gênero, faixa etária e cidade.
    """

    total_clients = df["cliente_id"].nunique()

    # --------------------
    # GÊNERO
    # --------------------
    gender_counts = df.groupby("genero_cliente")["cliente_id"].nunique()
    gender_percent = (gender_counts / total_clients * 100).round(2)

    genero = gender_percent.to_dict()

    # --------------------
    # FAIXA ETÁRIA
    # --------------------
    def faixa_etaria(idade):
        if idade < 18:
            return "menor_idade"
        elif idade <= 25:
            return "jovem"
        elif idade <= 40:
            return "adulto"
        elif idade <= 60:
            return "meia_idade"
        else:
            return "idoso"

    # Cria a coluna de faixa etária
    df = df.copy()
    df["faixa_etaria"] = df["idade_cliente"].apply(faixa_etaria)

    age_counts = df.groupby("faixa_etaria")["cliente_id"].nunique()
    age_percent = (age_counts / total_clients * 100).round(2)

    # --------------------
    # CIDADE
    # --------------------
    city_counts = df.groupby("cidade_cliente")["cliente_id"].nunique()
    city_percent = (city_counts / total_clients * 100).round(2)

    return {
        "genero": genero,
        "faixa_etaria": age_percent.to_dict(),
        "cidade": city_percent.to_dict()
    }
