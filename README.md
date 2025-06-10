## 📜 Sumário

  * [Visão Geral do Projeto](https://www.google.com/search?q=%23-vis%C3%A3o-geral-do-projeto)
  * [Integrantes do Grupo](https://www.google.com/search?q=%23-integrantes-do-grupo)
  * [Arquitetura e Funcionamento](https://www.google.com/search?q=%23-arquitetura-e-funcionamento)
  * [Imagens da Simulação](https://www.google.com/search?q=%23-imagens-da-simula%C3%A7%C3%A3o)
  * [Sensores Virtuais](https://www.google.com/search?q=%23-sensores-virtuais)
  * [Código-Fonte](https://www.google.com/search?q=%23-c%C3%B3digo-fonte)
  * [Análise Exploratória Inicial](https://www.google.com/search?q=%23-an%C3%A1lise-explorat%C3%B3ria-inicial)
  * [Regras Gerais](https://www.google.com/search?q=%23-regras-gerais)

-----

## 🏭 Visão Geral do Projeto

Este projeto visa a aplicação de conceitos de Inteligência Artificial e IoT para a **prevenção de falhas em linhas de produção industriais**. O sistema simula a coleta de dados de sensores em tempo real, armazena essas informações e utiliza algoritmos para detectar padrões que indiquem possíveis falhas, gerando alertas, dashboards e relatórios automatizados.

O principal problema que o projeto busca solucionar são as **interrupções inesperadas** em linhas de produção, que causam perdas financeiras, atrasos e aumento de custos com manutenção. A solução proposta é um **sistema inteligente de monitoramento preditivo** que utiliza dados de sensores para uma abordagem proativa na detecção de falhas.

-----

## 👥 Integrantes do Grupo

Matheus Parra - RM561907
Otavio Custodio de Oliveira - RM565606
Tiago Alves Cordeiro - RM561791
Thiago Henrique Pereira de Almeida Santos - RM563327
Leandro Arthur Marinho Ferreira - RM565240

-----

## 🧠 Arquitetura e Funcionamento

O sistema é composto por um backend em **Flask (Python)** que recebe os dados simulados dos sensores. Esses dados são armazenados em um banco de dados **Supabase**, e um frontend em **React** exibe as informações em um dashboard interativo.

O pipeline de dados é o seguinte:

1.  **Simulação de sensores (ESP32):** Scripts em Python geram dados periódicos de temperatura, vibração e umidade, imitando o comportamento de sensores reais.
2.  **API Flask:** Recebe e valida os dados via requisições HTTP.
3.  **Banco de Dados (Supabase):** Armazena os dados históricos para análise.
4.  **Dashboard (React):** Interface de visualização dos dados em tempo real, com alertas e gráficos.

-----

## 🖼️ Imagens da Simulação

As imagens da simulação do circuito e do comportamento do sistema (Monitor Serial, simulação de dados) podem ser encontradas na pasta `hardware/`.

*(Nota: A pasta hardware não foi encontrada no repositório fornecido. Adicione as imagens nesta seção quando disponíveis.)*

-----

## 🤖 Sensores Virtuais

Para a simulação, foram utilizados os seguintes sensores virtuais, que representam dados críticos em um ambiente industrial:

  * **Sensor de Temperatura:** Monitora a temperatura das máquinas, com alertas para valores acima de 85°C (aviso) e 95°C (crítico). O script de simulação gera valores de temperatura que podem chegar a 110°C para simular anomalias.
  * **Sensor de Vibração:** Mede a vibração nos eixos X, Y e Z. A média dos três eixos é utilizada para gerar alertas para valores acima de 2500 unidades ADC (aviso) e 3000 unidades ADC (crítico).
  * **Sensor de Umidade:** Monitora a umidade relativa do ambiente, com valores simulados entre 30% e 70%.
  * **Sensor de Rotação (RPM):** Calculado com base na vibração, com alertas para valores abaixo de 1600 RPM ou acima de 1950 RPM.

A escolha destes sensores se justifica pela sua relevância na detecção precoce de problemas comuns em equipamentos industriais, como superaquecimento, desgaste de peças e desalinhamento.

-----

## 💻 Código-Fonte

O código-fonte do projeto está organizado da seguinte forma:

  * `api-flask/app.py`: Contém a API Flask responsável por receber os dados dos sensores e armazená-los no banco de dados.
  * `src/lib/supabaseClient.ts`: Realiza a conexão com o banco de dados Supabase e define os tipos de dados.
  * `src/hooks/useSupabaseData.ts`: Hook do React para buscar e processar os dados do Supabase, além de gerar os alertas.
  * `src/components/Dashboard.tsx`: Componente principal do dashboard que exibe os dados e alertas.

O código está comentado para facilitar o entendimento da lógica de funcionamento.

-----

## 📊 Análise Exploratória Inicial

A análise inicial dos dados simulados nos permite extrair os seguintes insights:

  * **Correlação entre Vibração e RPM:** Conforme implementado no *hook* `useSupabaseData.ts`, existe uma relação direta entre os valores de vibração e o cálculo do RPM, o que permite inferir a rotação do equipamento a partir dos dados de vibração.
  * **Detecção de Anomalias de Temperatura:** O sistema é capaz de identificar picos de temperatura que ultrapassam os limites de segurança (85°C para aviso e 95°C para estado crítico), gerando alertas que podem ser visualizados no dashboard.
  * **Visualização de Tendências:** Os gráficos no painel de "Análise de Tendências" permitem observar o comportamento dos sensores ao longo do tempo, facilitando a identificação de padrões que possam indicar uma futura falha.

