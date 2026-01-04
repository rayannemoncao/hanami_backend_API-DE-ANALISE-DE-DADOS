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

## 📊 Relatórios Analíticos

Os relatórios gerados pela API incluem:

- Total de registros processados
- Métricas estatísticas básicas:
  - Soma
  - Média
  - Valor mínimo
  - Valor máximo
- Metadados do processamento
- Versão do algoritmo utilizado

Todos os relatórios são **versionados**, garantindo rastreabilidade e consistência dos resultados ao longo do tempo.

---

## 📖 Documentação da API

A documentação completa dos endpoints está disponível em:

/docs

---

A API segue o padrão **Swagger/OpenAPI**, contendo:

- Lista de endpoints disponíveis
- Parâmetros de entrada
- Exemplos de requisições e respostas

---

## 🪵 Logs

A aplicação registra automaticamente:

- Eventos importantes do sistema
- Erros de validação de dados
- Falhas durante o processamento

Os arquivos de log ficam disponíveis no diretório:

/logs

---


## ✅ Boas Práticas Adotadas

- Validação de dados antes de qualquer cálculo
- Separação clara de responsabilidades
- Versionamento de artefatos gerados
- Documentação contínua do projeto
- Código organizado, legível e escalável

---

## 📄 Licença

Este projeto é destinado a fins **educacionais e experimentais**.

---

## ✍️ Autoria

Desenvolvido por **Rayanne**  
Projeto criado com foco em aprendizado, construção de portfólio e evolução técnica.
