import pandas as pd 
from src.api.enginie_calculation import calculate_financial_metrics, calculate_sales_metrics

def test_calculate_financial_metrics():
    df = pd.DataFrame({
        "valor_final": [100, 200],
        "deducoes": [10, 20],
        "preco_unitario": [30, 40],
        "quantidade": [1, 2]
    })
    resultado = calculate_financial_metrics (df)
    assert resultado["receita_bruta"] == 300
    assert resultado["receita_liquida"] == 270
    assert resultado["lucro_bruto"] == 160
    print(resultado)

def test_calculate_sales_metrics():
    df = pd.DataFrame({
        "id_transacoes": [1, 2, 3],
        "valor_final": [100, 200, 300],
        "deducoes": [10, 20, 30]
    })
    resultado = calculate_sales_metrics (df)
    assert resultado["total_vendas"] == 3
    assert resultado["ticket_medio"] == 180 # (100+200+300 - (10+20+30)) / 3                
    print(resultado)