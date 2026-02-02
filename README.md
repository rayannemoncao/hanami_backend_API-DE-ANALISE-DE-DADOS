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

- **Linguagem:** Python  
- **Framework da API:** FastAPI  
- **Documentação:** Swagger / OpenAPI  
- **Análise de dados:** Pandas  
- **Geração de relatórios:** ReportLab  
- **Controle de versão:** Git  
- **Formatos suportados:** CSV, XLSX  

---

## 📂 Estrutura do Projeto

```text
.
HANAMI/
├── docs/                     # Documentação do projeto
├── logs/                     # Logs da aplicação
├── src/
│   ├── api/
│   │   ├── routes/           # Endpoints da API
│   │   │   ├── upload.py
│   │   │   ├── analytics.py
│   │   │   ├── products.py
│   │   │   ├── demography.py
│   │   │   └── reports.py
│   │   └── main.py           # Ponto de entrada da aplicação
│   ├── services/             # Regras de negócio e cálculos
│   ├── parsers/              # Tratamento e transformação de dados
│   ├── runtime_data/         # Arquivos processados em tempo de execução
│   └── utils/                # Funções utilitárias
├── tests/                    # Testes automatizados
├── venv/                     # Ambiente virtual
├── .gitignore
└── README.md


```
---

## 📤 Upload de Arquivos

A API aceita arquivos nos formatos:

- `.csv`
- `.xlsx`

Os arquivos passam pelas seguintes etapas:

- Validação do tipo de arquivo
- Armazenamento temporário
- Preparação para análise
- Registro de logs de processamento

---

## 📊 Analytics

O módulo de **Analytics** realiza cálculos automáticos a partir do **arquivo mais recente processado**, incluindo:

- Receita bruta
- Receita líquida
- Lucro bruto
- Total de vendas
- Ticket médio

Os resultados são retornados em formato **JSON** por meio de um endpoint dedicado.

---

## 📑 Relatórios

A API permite a geração de **relatórios analíticos** nos formatos:

- **JSON**
- **PDF**

Os relatórios consolidam os dados processados e as métricas calculadas.

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
pip install fastapi uvicorn pandas openpyxl reportlab
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
