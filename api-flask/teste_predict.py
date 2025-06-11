import requests
import json

# URL do endpoint de predição
url = "http://127.0.0.1:5000/predict"

# Dados dos sensores para enviar
dados_para_predicao = {
    "temperatura": 98.5,
    "vibracao_x": 3100,
    "vibracao_y": 3250,
    "vibracao_z": 3300,
    "umidade": 45.2
}

# Cabeçalho da requisição
headers = {
    "Content-Type": "application/json"
}

# Faz a requisição POST
try:
    response = requests.post(url, data=json.dumps(dados_para_predicao), headers=headers)
    response.raise_for_status()  # Lança uma exceção para respostas de erro (4xx/5xx)
    
    # Imprime a resposta da API
    resultado = response.json()
    print("Resposta da API:", resultado)
    
except requests.exceptions.RequestException as e:
    print(f"Erro ao fazer a requisição: {e}")