
# 🏭 Sistema de Prevenção de Falhas em Linhas de Produção Industrial

## 📌 Visão Geral

Este projeto foi desenvolvido como parte do desafio proposto pela empresa **Hermes Reply**, com o objetivo de aplicar Inteligência Artificial e IoT na **prevenção de falhas em linhas de produção industriais**. O sistema simula a coleta de dados em tempo real via sensores (ESP32), armazena essas informações em um banco de dados na nuvem e utiliza algoritmos de Machine Learning para detectar padrões que indiquem possíveis falhas, gerando **alertas, dashboards e relatórios automatizados** para a equipe técnica.

## 🎯 Problema

Empresas industriais sofrem com **interrupções inesperadas** nas linhas de produção, causadas por falhas mecânicas e elétricas em seus equipamentos. Essas paradas geram:

- Perdas financeiras;
- Atrasos logísticos;
- Aumento do custo de manutenção corretiva;
- Redução da produtividade e da eficiência operacional.

**A ausência de uma abordagem preditiva** dificulta a detecção precoce dessas falhas, limitando a atuação apenas após o problema ocorrer.

## 💡 Solução Proposta

Criar um **sistema inteligente de monitoramento preditivo**, baseado em:

- **Coleta de dados via sensores IoT (ESP32)**;
- Armazenamento em **banco de dados na nuvem (AWS RDS)**;
- Processamento com **modelos de Machine Learning (Scikit-learn, TensorFlow)**;
- Visualização via **dashboards (Grafana ou Power BI)**;
- Geração de **alertas automáticos** para manutenção preventiva.

## 🧰 Tecnologias Utilizadas

| Tecnologia        | Função                                                             |
|------------------|--------------------------------------------------------------------|
| **Python 3.x**    | Lógica de backend e scripts de análise preditiva                  |
| **Flask**         | API REST para recebimento dos dados dos sensores                  |
| **ESP32 (simulado)** | Simulação da coleta de dados via sensores IoT                    |
| **Pandas / NumPy**| Processamento e análise dos dados coletados                       |
| **Scikit-learn**  | Modelagem preditiva com algoritmos de ML                          |
| **TensorFlow**    | Suporte a modelos mais complexos, se necessário                   |
| **AWS RDS**       | Banco de dados relacional para armazenamento dos dados            |
| **AWS EC2**       | Processamento dos dados e execução dos modelos de IA              |
| **Grafana / Power BI** | Criação dos dashboards de visualização em tempo real         |
| **Draw.io**       | Ferramenta usada para criação do diagrama da arquitetura          |

## 🧠 Arquitetura da Solução

```
graph TD
    A[ESP32 - Sensores] --> B[API Flask (Python)]
    B --> C[Banco de Dados (AWS RDS)]
    C --> D[Processamento de IA (AWS EC2)]
    D --> E[Dashboards (Grafana / Power BI)]
    D --> F[Alertas e Relatórios Automáticos]
```

## 🔁 Pipeline de Dados

1. **Simulação de sensores IoT (ESP32):** geração periódica de dados simulados (temperatura, vibração, rotação, etc.).
2. **API Flask:** recebe e valida os dados via requisições HTTP.
3. **Banco de dados AWS RDS:** armazena os dados com histórico e metadata.
4. **Processamento em EC2 (AWS):** scripts em Python acessam os dados e aplicam modelos de Machine Learning para detectar padrões.
5. **Dashboards e Relatórios:** interface de visualização dos dados, com alertas e relatórios enviados periodicamente.

## 🔎 Estratégia de Coleta de Dados

- Nesta fase, os dados serão **simulados** com base em cenários industriais reais.
- A simulação é feita com **geradores de dados em Python**, que imitam o comportamento esperado de sensores ESP32 conectados a motores, esteiras e máquinas industriais.
- No futuro, será possível integrar diretamente com sensores físicos via comunicação MQTT ou HTTP, utilizando microcontroladores como o ESP32.



## 📂 Organização do Repositório

```
📁 /src
├── /api_flask/
├── /simulador/
├── /modelos/
├── /dashboards/
📁 /docs
├── arquitetura.drawio
├── README.md
└── plano_de_desenvolvimento.md
```

