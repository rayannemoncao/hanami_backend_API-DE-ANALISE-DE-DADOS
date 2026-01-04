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
├── src/
│   ├── api/          # Endpoints e controllers
│   ├── services/     # Regras de negócio e análises
│   ├── parsers/      # Leitura e validação de CSV/XLSX
│   ├── models/       # Estruturas de dados
│   └── utils/        # Funções auxiliares
├── docs/             # Documentação técnica e da API
├── logs/             # Logs da aplicação
├── tests/            # Testes automatizados
├── .gitignore
├── README.md
└── .env.example
