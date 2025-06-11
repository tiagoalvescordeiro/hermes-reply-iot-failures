
# Sistema de Monitoramento Preditivo para Linhas de Produção

Este projeto é um sistema inteligente de monitoramento industrial que utiliza conceitos de IoT e Inteligência Artificial para prever e prevenir falhas em equipamentos, otimizando a manutenção e reduzindo paradas inesperadas na linha de produção.

---

## 📜 Sumário

- [Visão Geral do Projeto](#-visão-geral-do-projeto)
- [O Problema](#-o-problema)
- [A Solução](#-a-solução)
- [Principais Funcionalidades](#-principais-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Arquitetura da Solução](#-arquitetura-da-solução)
- [Como Executar o Projeto](#-como-executar-o-projeto)
  - [Pré-requisitos](#-pré-requisitos)
  - [Configuração do Banco de Dados (Supabase)](#-configuração-do-banco-de-dados-supabase)
  - [Configuração do Backend (API Flask)](#-configuração-do-backend-api-flask)
  - [Configuração do Frontend (React)](#-configuração-do-frontend-react)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Lógica de Alertas e Predição](#-lógica-de-alertas-e-predição)
- [Integrantes do Grupo](#-integrantes-do-grupo)

---

## 🏭 Visão Geral do Projeto

Este projeto foi desenvolvido como parte de um desafio para aplicar Inteligência Artificial e IoT na **prevenção de falhas em linhas de produção industriais**. O sistema simula a coleta de dados de sensores em tempo real, armazena essas informações em um banco de dados na nuvem (Supabase) e utiliza algoritmos para detectar padrões que indiquem possíveis falhas, gerando alertas, dashboards interativos e relatórios automatizados.

## 🎯 O Problema

Interrupções inesperadas em linhas de produção, causadas por falhas de equipamento, geram perdas financeiras, atrasos na produção e aumento nos custos de manutenção. A ausência de uma abordagem preditiva limita as equipes a atuarem apenas de forma reativa, ou seja, após a ocorrência do problema.

## 💡 A Solução

A solução proposta é um **sistema inteligente de monitoramento preditivo** que combina hardware simulado e uma stack de software moderna. O sistema coleta e analisa dados de sensores para identificar anomalias e prever falhas antes que elas aconteçam, permitindo uma manutenção proativa. A plataforma é composta por um dashboard em React que exibe dados em tempo real, um backend em Flask (Python) para processamento e uma base de dados no Supabase para armazenamento.

## ✨ Principais Funcionalidades

- **Dashboard Interativo:** Visualização em tempo real dos dados dos sensores de múltiplas máquinas com status, alertas e gráficos de tendência.
- **Alertas Automatizados:** O sistema gera alertas de "Aviso" e "Crítico" com base em limites pré-configurados de temperatura e vibração.
- **Análise de Tendências:** Gráficos históricos que permitem a visualização do comportamento dos sensores ao longo do tempo, facilitando a identificação de padrões de falha.
- **Previsão de Falhas com Machine Learning:** Um endpoint na API utiliza um modelo de Machine Learning (`RandomForestClassifier`) para prever a probabilidade de falha de um equipamento com base nos dados recebidos.
- **Simulação de Sensores:** Scripts para simular o envio de dados de sensores de temperatura, umidade e vibração, imitando um ambiente de hardware com ESP32.

## 🛠️ Tecnologias Utilizadas

| Categoria      | Tecnologia                                                                                                  |
| :------------- | :---------------------------------------------------------------------------------------------------------- |
| **Frontend** | `React`, `Vite`, `TypeScript`, `TailwindCSS`, `Shadcn/ui`, `Recharts`, `React Query` |
| **Backend** | `Python`, `Flask`, `Pandas`, `Scikit-learn`                                                |
| **Banco de Dados** | `Supabase` (PostgreSQL)                                                                                     |
| **Simulação** | `Wokwi` para simulação de hardware (ESP32)                                                               |

## 🧠 Arquitetura da Solução

O sistema possui a seguinte arquitetura de dados:

1.  **Simulação de Sensores (`simulator.py`)**: Scripts em Python geram dados periódicos (temperatura, umidade, vibração) e os enviam para a API, simulando o comportamento de sensores IoT como um ESP32.
2.  **API Backend (`api-flask/app.py`)**: Uma API em Flask recebe os dados via requisições HTTP, processa-os e os armazena no banco de dados Supabase. Ela também possui um endpoint `/predict` para predição de falhas.
3.  **Banco de Dados (Supabase)**: Um banco de dados PostgreSQL gerenciado pelo Supabase armazena os dados das máquinas e as leituras históricas dos sensores.
4.  **Frontend (React)**: Um dashboard construído em React com a biblioteca de componentes `shadcn/ui` busca os dados do Supabase em tempo real e os exibe em uma interface intuitiva, com cartões de status, alertas e gráficos.

```mermaid
graph TD
    A[Simulador de Sensores] -- Dados JSON via HTTP --> B[API Flask (Python)];
    B -- Armazena Leituras --> C[Banco de Dados Supabase];
    D[Dashboard React] -- Busca Dados --> C;
    B -- /predict --> E[Modelo de ML];
```

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### 1. Pré-requisitos

- Node.js e npm (ou Yarn/pnpm)
- Python 3.x e pip
- Uma conta no [Supabase](https://supabase.com)

### 2. Configuração do Banco de Dados (Supabase)

1.  **Crie um novo projeto no Supabase** e guarde a **Project URL** e a **anon/public key** da API.
2.  No editor SQL do Supabase, execute o script de schema para criar as tabelas necessárias. O schema pode ser encontrado em `scripts/database-schema.sql` ou `supabase/migrations/20250610213345-17113cf8-abe6-4158-ac5c-9e90ecddc917.sql`.

### 3. Configuração do Backend (API Flask)

1.  Navegue até a pasta `api-flask`:
    ```bash
    cd api-flask
    ```
2.  Crie um ambiente virtual e instale as dependências:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
3.  Crie um arquivo `.env` na pasta `api-flask` e adicione as suas credenciais do Supabase:
    ```env
    SUPABASE_URL=SUA_PROJECT_URL_AQUI
    SUPABASE_KEY=SUA_ANON_KEY_AQUI
    ```
4.  **Treine o modelo de Machine Learning** (Opcional, um modelo pré-treinado pode estar incluído):
    ```bash
    python treinar_modelo.py
    ```
    Isso irá gerar o arquivo `failure_model.pkl`.

5.  **Inicie a API Flask**:
    ```bash
    flask run --reload
    ```
    A API estará rodando em `http://127.0.0.1:5000`.

### 4. Configuração do Frontend (React)

1.  Na raiz do projeto, instale as dependências do Node.js:
    ```bash
    npm install
    ```
2.  Crie um arquivo `.env.local` na raiz do projeto e adicione suas credenciais do Supabase:
    ```env
    VITE_SUPABASE_URL=SUA_PROJECT_URL_AQUI
    VITE_SUPABASE_ANON_KEY=SUA_ANON_KEY_AQUI
    ```
3.  **Popule o banco de dados** com dados de exemplo (opcional, mas recomendado):
    ```bash
    npm run seed
    ```
    Este script irá criar 3 máquinas de exemplo e leituras de sensores para as últimas 24 horas.

4.  **Inicie a aplicação React**:
    ```bash
    npm run dev
    ```
    O dashboard estará acessível em `http://localhost:8080`.

### 5. Simulação de Dados

Para enviar dados continuamente para a API, você pode usar o simulador:

1.  Certifique-se de que a API Flask está rodando.
2.  Em um novo terminal, navegue até `api-flask` e execute o simulador:
    ```bash
    python simulator.py
    ```
    O simulador irá enviar dados para as máquinas cadastradas a cada 25 segundos.

## 📂 Estrutura do Repositório

```
/
├── api-flask/            # Backend em Flask e scripts de simulação/treinamento
│   ├── app.py            # Arquivo principal da API
│   ├── simulator.py      # Script para simular dados de sensores
│   ├── treinar_modelo.py # Script para treinar o modelo de ML
│   └── requirements.txt  # Dependências do Python
├── public/               # Arquivos estáticos
├── scripts/              # Scripts para setup e popular o banco de dados
│   ├── database-schema.sql # Schema do banco
│   └── seed.ts           # Script para popular o banco
├── src/                  # Código-fonte do frontend em React
│   ├── components/       # Componentes da UI (Dashboard, Gráficos, Alertas)
│   ├── hooks/            # Hooks customizados (ex: useSupabaseData)
│   ├── lib/              # Funções utilitárias e cliente Supabase
│   └── pages/            # Páginas da aplicação
├── README.md             # Este arquivo
└── package.json          # Dependências e scripts do frontend
```

## 📈 Lógica de Alertas e Predição

O sistema utiliza as seguintes regras para gerar alertas e predições:

- **Temperatura**:
  - **Aviso**: > 85°C
  - **Crítico**: > 95°C
- **Vibração (média dos 3 eixos)**:
  - **Aviso**: > 2500 unidades ADC
  - **Crítico**: > 3000 unidades ADC
- **RPM (calculado com base na vibração)**:
  - **Aviso**: < 1600 RPM ou > 1950 RPM
- **Previsão de Falha (IA)**:
  - Um modelo `RandomForestClassifier` é treinado com dados históricos para prever a probabilidade de falha com base na temperatura, vibração e umidade atuais.

## 👥 Integrantes do Grupo

- Matheus Parra - RM561907
- Otavio Custodio de Oliveira - RM565606
- Tiago Alves Cordeiro - RM561791
- Thiago Henrique Pereira de Almeida Santos - RM563327
