import pandas as pd

# Função usada para ler o arquivo, validar e devolver dados confiáveis. Será usada em toda a API.
# Como parametro recebe o caminho do arquivo e uma array de str contendo as colunas a serem trabalhadas.
def read_and_validate(file_path: str, columns):
#Garante que só formatos aceitos entrem no sistema, no caso vai ler CSV ou XLSX
    if file_path.endswith(".csv"):
        df=pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        df=pd.read_excel(file_path)
    else:
        raise ValueError("Formato inválido. Envie um arquivo CSV ou XLSX.")


    #Verifica se todas as colunas existem
    missing_columns = [
        col for col in columns if col not in df.columns
    ]
    if missing_columns:
        raise ValueError(f"O arquivo não contém todas as colunas obrigatórias:{missing_columns}")


    #Limpa dados nulos - campos que não podem ser nulos (linhas incompletas são removidas)
    null_columns = [
        "id_transacao",
        "data_venda",
        "valor_final",
        "cliente_id",
        "produto_id",
        "quantidade"
    ]

    #Converte campos numéricos
    numeric_columns = [
        "valor_final",
        "subtotal",
        "desconto_percent",
        "idade_cliente",
        "renda_estimada",
        "preco_unitario",
        "quantidade",
        "margem_lucro",
        "tempo_entrega_dias"
    ]
    #conversao
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    #remove linhas invalidas
    df = df.dropna(subset=numeric_columns)

    #Converte campo data
    df["data_venda"] = pd.to_datetime(
    df["data_venda"], errors = "coerce"
    )
    df = df.dropna(subset=["data_venda"])

    #Padroniza o texto
    text_columns = [
        "canal_venda",
        "forma_pagamento",
        "genero_cliente",
        "cidade_cliente",
        "estado_cliente",
        "categoria",
        "marca",
        "regiao",
        "status_entrega"
    ]

    for col in text_columns:
        df[col] = (
        df[col]
        .astype(str)
        .str.lower()
        .str.strip()
    )

    #retorna o dataframe limpo

    return df