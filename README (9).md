
# Hermes Reply – Simulação de Falhas com IoT e Modelo Preditivo

Este projeto simula um sistema embarcado com ESP32 e sensores virtuais para coleta de dados industriais, com foco em predição de falhas usando Machine Learning (Random Forest) integrado a uma API Flask.

---

## 📦 Estrutura da Pasta

```
hermes-api/
├── app.py                # API Flask
├── failure_model.pkl     # Modelo preditivo treinado (Random Forest)
├── sensor_data.csv       # Dados simulados dos sensores
└── treinar_modelo.py     # Script para treinar o modelo localmente
```

---

## ⚙️ Etapas do Projeto

### 1. Simulação de Dados
Sensores simulados:
- Temperatura
- Vibração (vib_x, vib_y, vib_z → média)
- Umidade
- RPM

Critérios de falha:
- Temperatura > 95°C
- Vibração > 3000 (média)

Os dados foram salvos em `sensor_data.csv`.

---

### 2. Treinamento do Modelo

Para reprocessar ou adaptar o modelo ao seu ambiente local:

```bash
py treinar_modelo.py
```

Isso gera o arquivo `failure_model.pkl`.

---

### 3. Execução da API Flask

Inicie a API com:

```bash
py app.py
```

A API estará acessível em:

```
http://127.0.0.1:5000/
```

---

### 4. Teste da Predição

#### 🔹 Usando PowerShell (Windows):

```powershell
curl -Method POST http://127.0.0.1:5000/predict -Headers @{"Content-Type"="application/json"} -Body '{"temp": 98, "vibration": 3200, "humidity": 60, "rpm": 1450}'
```

#### 🔹 Usando Postman:
- Método: `POST`
- URL: `http://127.0.0.1:5000/predict`
- Body > raw > JSON:
```json
{
  "temp": 98,
  "vibration": 3200,
  "humidity": 60,
  "rpm": 1450
}
```

Resposta esperada:
```json
{
  "falha_prevista": true,
  "probabilidade_falha": 0.92
}
```

---

## 🧠 Modelo Utilizado

- Algoritmo: `RandomForestClassifier`
- Features: `temp`, `vibration`, `humidity`, `rpm`
- Target: `failure` (0 ou 1)
- Acurácia simulada: ~100% (ambiente controlado)

---

## 📸 Prints Recomendados para o GitHub

- Interface do VS Code com arquivos (`app.py`, `sensor_data.csv`, etc)
- Execução do terminal com `py app.py`
- Resultado no navegador (`127.0.0.1:5000`)
- Teste via PowerShell ou Postman

---

## ✍️ Autores

Projeto desenvolvido como parte do Desafio Hermes Reply (FIAP – Fase 4 – Sprint 2).
