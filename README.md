# Projeto Hanami — Backend API de Análise de Dados

## 📌 Visão Geral

O **Projeto Hanami** é uma API backend desenvolvida para **processar arquivos CSV e XLSX**, realizar **análises de dados** e gerar **relatórios analíticos estruturados**, de forma segura, versionada e documentada.

O foco do projeto é garantir:
- Processamento robusto de dados
- Validação e padronização antes de cálculos
- Arquitetura organizada e escalável
- Documentação clara para fácil reprodução do ambiente

---

## 🎯 Objetivo

Desenvolver uma **API robusta** capaz de:
- Receber uploads de arquivos CSV e XLSX
- Realizar parsing e validação de dados
- Executar análises estatísticas iniciais
- Gerar relatórios analíticos versionados
- Disponibilizar resultados via endpoints REST

---

## 🛠️ Tecnologias Utilizadas

> Ajuste conforme o stack escolhido

- Linguagem: `Python `
- Framework de API: `FastAPI `
- Documentação: `Swagger / OpenAPI`
- Controle de versão: `Git`
- Formatos suportados: `CSV`, `XLSX`

---

## 📂 Estrutura do Projeto

```text
.
HANAMI/
├── docs/                  # Documentação do projeto
├── logs/                  # Logs da aplicação
├── src/
│   ├── api/
│   │   ├── main.py        # Ponto de entrada da API
│   │   ├── data_reader.py # Leitura e validação de arquivos
│   │   └── app.log        # Log da aplicação
│   ├── models/            # Modelos de dados
│   ├── parsers/           # Parsers e transformações
│   ├── services/          # Regras de negócio
│   └── utils/             # Funções utilitárias
├── tests/
│   ├── test_data_reader.py
│   └── vendas_ficticias_10000_linhas.csv
├── venv/                  # Ambiente virtual
├── .gitignore
└── README.md

```
---

## 📤 Upload de Arquivos

A API aceita arquivos nos formatos:
- `.csv`
- `.xlsx`

Os arquivos passam por:
- Validação de tipo e tamanho
- Padronização de dados
- Registro de logs

---

## 🐍 Pré-requisitos

- Python 3.10 ou superior  
- Git

---

## 🚀 Setup do Ambiente

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/rayannemoncao/hanami_backend_API-DE-ANALISE-DE-DADOS
cd HANAMI
```

### 2️⃣ Criar e ativar ambiente virtual (Python)
```bash
python -m venv venv
```

Ativar o ambiente virtual:
- **Windows**
```bash
venv\Scripts\activate
```

- **Linux / macOS**
```bash
source venv/bin/activate
```

### 4️⃣ Instalar dependências
```bash
pip install fastapi uvicorn pandas openpyxl
```

### ▶️ Executando o Projeto
```bash
uvicorn src.api.main:app --reload
```
---

## 🌐 Acessos da Aplicação
```bash
API: http://127.0.0.1:8000
Documentação Swagger: http://127.0.0.1:8000/docs
```
---

## 🧾 Logs da Aplicação

Logs gravados em: 
```bash
src/api/app.log
```
Níveis de log utilizados:
INFO: fluxo normal da aplicação
ERROR: erros de validação ou processamento

---

## 📌 Observações

- Os arquivos enviados são processados em diretórios temporários
- O sistema valida colunas obrigatórias e tipos de dados
- Arquivos temporários são removidos automaticamente após o processamento

---

## 📄 Licença

Este projeto é destinado a fins **educacionais e experimentais**.

---

## ✍️ Autoria

Desenvolvido por **Rayanne**  
Projeto criado com foco em aprendizado, construção de portfólio e evolução técnica.
