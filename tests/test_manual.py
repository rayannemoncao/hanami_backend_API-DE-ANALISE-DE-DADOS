import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from src.services.demography_and_region import (
    metrics_by_region,
    demographic_distribution
)

# 1️⃣ Cria um DataFrame fake (dados de exemplo)
data = {
    "id_transacao": [1, 2, 3, 4],
    "valor_final": [100, 200, 150, 50],
    "regiao": ["sul", "sul", "norte", "norte"],
    "cliente_id": [10, 11, 10, 12],
    "genero_cliente": ["f", "m", "f", "m"],
    "idade_cliente": [25, 40, 30, 70],
    "cidade_cliente": ["porto alegre", "porto alegre", "manaus", "manaus"]
}

df = pd.DataFrame(data)

# 2️⃣ Testa métricas por região
print("📊 MÉTRICAS POR REGIÃO")
print(metrics_by_region(df))

# 3️⃣ Testa distribuição demográfica
print("\n👥 DISTRIBUIÇÃO DEMOGRÁFICA")
print(demographic_distribution(df))
