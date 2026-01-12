#importa ferramentas de sistema (caminhos e configurações)
import sys
import os

#adiciona a pasta raiz do projeto à lista de caminhos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.parsers.data_reader import read_and_validate

print("🚀 Script iniciado com sucesso")

caminho_arquivo = "tests/vendas_ficticias_10000_linhas.csv"

try:
    required_columns = [
    # Vendas e transações
    "id_transacao",
    "data_venda",
    "valor_final",
    "subtotal",
    "desconto_percent",
    "canal_venda",
    "forma_pagamento",

    # Clientes
    "cliente_id",
    "nome_cliente",
    "idade_cliente",
    "genero_cliente",
    "cidade_cliente",
    "estado_cliente",
    "renda_estimada",

    # Produtos
    "produto_id",
    "nome_produto",
    "categoria",
    "marca",
    "preco_unitario",
    "quantidade",
    "margem_lucro",

    # Logística
    "regiao",
    "status_entrega",
    "tempo_entrega_dias",
    "vendedor_id"

    #Se faltar qualquer uma dessas colunas apresentará erro imediato
]
    df = read_and_validate(caminho_arquivo, required_columns)
    print("✅ Arquivo lido com sucesso!")
    print(f"Total de linhas válidas: {len(df)}")
    print("\nPrimeiras linhas dos dados:")
    print(df.head())
except Exception as e:
    print("❌ Erro ao processar o arquivo:")
    print(e)
