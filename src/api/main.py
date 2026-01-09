# importa ferramentas para criar a API e receber arquivos
from typing_extensions import Annotated
from fastapi import FastAPI, UploadFile, File, HTTPException, Request
# Salva o arquivo recebido temporariamente no computador, lê e valida os dados
import tempfile
import os
import pandas as pd
import logging 

# Configuração do logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Função usada para ler o arquivo, validar e devolver dados confiáveis. Será usada em toda a API.
def read_and_validate(file_path: str, columns):
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)
    #Seu formato não é aceito, lança erro e encerra a execução lançando exceção.
    else:
        logger.error("Formato inválido. Envie um arquivo CSV ou XLSX.")
        raise Exception("Formato inválido. Envie um arquivo CSV ou XLSX.")

    missing_columns = [col for col in columns if col not in df.columns]
    if missing_columns:
        logger.error(f"O arquivo não contém todas as colunas obrigatórias:{missing_columns}")
        raise Exception(f"O arquivo não contém todas as colunas obrigatórias:{missing_columns}")

    numeric_columns = [
        "valor_final", "subtotal", "desconto_percent", "idade_cliente",
        "renda_estimada", "preco_unitario", "quantidade", "margem_lucro",
        "tempo_entrega_dias"
    ]
    for col in numeric_columns:
        #converte colunas para numericas, invalido vira NaN
        df[col] = pd.to_numeric(df[col], errors="coerce")
        #remove linhas com valores NaN nessas colunas
    df = df.dropna(subset=numeric_columns)

    df["data_venda"] = pd.to_datetime(df["data_venda"], errors="coerce")
    df = df.dropna(subset=["data_venda"])

    text_columns = [
        "canal_venda", "forma_pagamento", "genero_cliente", "cidade_cliente",
        "estado_cliente", "categoria", "marca", "regiao", "status_entrega"
    ]
    #converte tudo para texto minusculo e sem espaços desnecessarios
    for col in text_columns:
        df[col] = df[col].astype(str).str.lower().str.strip()
    #Retorna o dataframe limpo e validado
    return df

logger.info("Iniciando a API de Análise de Dados...")
#Colunas obrigatórias para validação
required_columns = [
    "id_transacao","data_venda","valor_final","subtotal","desconto_percent",
    "canal_venda","forma_pagamento","cliente_id","nome_cliente","idade_cliente",
    "genero_cliente","cidade_cliente","estado_cliente","renda_estimada",
    "produto_id","nome_produto","categoria","marca","preco_unitario","quantidade",
    "margem_lucro","regiao","status_entrega","tempo_entrega_dias","vendedor_id"
]
#Cria a API, aparece automaticamente na documentação /docs
app = FastAPI(
    title="HANAMI - API de Análise de Dados",
    description="API para upload e análise de arquivos CSV e XLSX",
    version="1.0.0"
)
# Teste basico para saber se a API está rodando
@app.get("/")
def hello():
    logger.info("Requisição recebida.")
    return {"message": "API de Análise de Dados está rodando!"}


@app.middleware("http")
async def log_request(request: Request, call_next):
    logger.info(f"Recebida requisição: {request.method} {request.url}")
    response = await call_next(request)
    return response

ALLOWED_EXTENSIONS = [".csv", ".xlsx"]

# Endpoint responsavel por upload de arquivos
@app.post("/upload")
async def upload_arquivo(file: UploadFile):
    logger.info(f"Recebido arquivo: {file.filename}")
    if not file.filename:
        # Nenhum arquivo enviado 400
        logger.error("Arquivo não enviado.")
        raise HTTPException(status_code=400, detail="Arquivo não enviado.")

    # Verifica a extensão do arquivo
    extensao = os.path.splitext(file.filename)[1].lower()
    if extensao not in ALLOWED_EXTENSIONS:
        # Tipo inválido 400
        logger.error("Tipo de arquivo não suportado. Envie um arquivo CSV ou XLSX.")
        raise HTTPException(status_code=400, detail="Tipo de arquivo não suportado. Envie um arquivo CSV ou XLSX.")

    # Lê o conteúdo do arquivo em bytes
    content = await file.read()
    logger.info(f"Tamanho do arquivo recebido: {len(content)} bytes")
    #fecha o arquivo após a leitura
    await file.close()

    #Cria um arquivo temporário para salvar o conteúdo e processar
    with tempfile.TemporaryDirectory() as tmpdir:
        #Cria o caminho temporário
        temp_path = os.path.join(tmpdir, file.filename)
        #Salva o conteúdo no arquivo temporário
        with open(temp_path, "wb") as temp_file:
            temp_file.write(content)

        #Lê, valida e trata o arquivo usando a função criada
        try:
            df = read_and_validate(temp_path, required_columns)
            logger.info(f"Arquivo processado: {file.filename}")
            return {
                "status": "sucesso",
                "mensagem": "Arquivo processado com sucesso.",
                "total_linhas_validas": len(df),
                "colunas": list(df.columns)
            }
        except ValueError as e:
            # Arquivo inválido 422
            logger.error("Erro ao processar o arquivo.")
            raise HTTPException(status_code=422, detail=f"Erro ao processar o arquivo: {str(e)}")
        #não precisa remover manualmente, o diretório temporário é apagado automaticamente TemporaryDirectory