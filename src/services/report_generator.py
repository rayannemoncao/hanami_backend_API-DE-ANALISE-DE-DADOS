import os
import json
import pandas as pd

# 🔥 ESSENCIAL para rodar em API / servidor sem interface gráfica
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Table,
    Image,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet

from src.services.demography_and_region import metrics_by_region


# =====================================================
# CAMINHOS BASE
# =====================================================
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RUNTIME_DIR = os.path.join(BASE_DIR, "runtime_data")
REPORTS_DIR = os.path.join(RUNTIME_DIR, "reports")

os.makedirs(REPORTS_DIR, exist_ok=True)

CHART_PATH = os.path.join(REPORTS_DIR, "vendas_por_regiao.png")
PDF_PATH = os.path.join(REPORTS_DIR, "report.pdf")
JSON_PATH = os.path.join(REPORTS_DIR, "report.json")


# =====================================================
# RELATÓRIO JSON
# =====================================================
def generate_json_report():
    df = _load_latest_dataframe()

    report = {
        "regional_performance": metrics_by_region(df),
        "total_linhas": int(len(df))
    }

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    return JSON_PATH


# =====================================================
# RELATÓRIO PDF (TABELA + GRÁFICO)
# =====================================================
def generate_pdf_report():
    df = _load_latest_dataframe()
    metrics = metrics_by_region(df)

    # 🔥 GERA O GRÁFICO ANTES DO PDF
    _generate_bar_chart(metrics)

    styles = getSampleStyleSheet()
    elements = []

    # TÍTULO
    elements.append(Paragraph("Relatório de Vendas por Região", styles["Title"]))
    elements.append(Spacer(1, 20))

    # TABELA
    table_data = [
        ["Região", "Total de Vendas", "Transações", "Ticket Médio"]
    ]

    for region, values in metrics.items():
        table_data.append([
            region,
            f"{values['total_vendas']:.2f}",
            values["quantidade_transacoes"],
            f"{values['ticket_medio']:.2f}"
        ])

    elements.append(Table(table_data))
    elements.append(Spacer(1, 30))

    # GRÁFICO
    if os.path.exists(CHART_PATH):
        elements.append(Paragraph("Gráfico: Vendas por Região", styles["Heading2"]))
        elements.append(Spacer(1, 15))
        elements.append(Image(CHART_PATH, width=400, height=300))

    doc = SimpleDocTemplate(PDF_PATH)
    doc.build(elements)

    return PDF_PATH


# =====================================================
# GERA GRÁFICO DE BARRAS
# =====================================================
def _generate_bar_chart(metrics: dict):
    regions = list(metrics.keys())
    totals = [v["total_vendas"] for v in metrics.values()]

    plt.figure(figsize=(6, 4))
    plt.bar(regions, totals)
    plt.title("Vendas por Região")
    plt.xlabel("Região")
    plt.ylabel("Total de Vendas")

    plt.tight_layout()
    plt.savefig(CHART_PATH)
    plt.close()


# =====================================================
# CARREGA ARQUIVO MAIS RECENTE (CSV ou XLSX)
# =====================================================
def _load_latest_dataframe() -> pd.DataFrame:
    files = [
        os.path.join(RUNTIME_DIR, f)
        for f in os.listdir(RUNTIME_DIR)
        if f.endswith((".csv", ".xlsx"))
    ]

    if not files:
        raise FileNotFoundError("Nenhum arquivo de dados encontrado.")

    latest_file = max(files, key=os.path.getctime)
    ext = os.path.splitext(latest_file)[1].lower()

    if ext == ".csv":
        return pd.read_csv(latest_file)
    elif ext == ".xlsx":
        return pd.read_excel(latest_file)
    else:
        raise ValueError("Formato de arquivo não suportado.")
