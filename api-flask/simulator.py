import requests
import random
import time
from datetime import datetime

# --- Configuração ---
# URL da sua API Flask que está rodando localmente
API_URL = "http://127.0.0.1:5000"

# Insira aqui os IDs das máquinas que você já tem no Supabase.
# Você pode obter os IDs diretamente da sua tabela 'maquinas' no Supabase.
IDS_DAS_MAQUINAS = [
    "008a31f1-2e1e-422f-a995-5534a11677b6",
    "18654713-2a1c-4bd1-aa49-090b8e788841",
    "451a95fa-06dc-46c9-9bbf-b5247ec5b38a",
    "7c15d379-4cd7-4df6-b71c-6302283a8d99",
    "808f6d4e-ac98-40b5-81f7-394687df14ef",
    "89e463bb-9490-4e66-bcdb-21db0b1748af",
    "be0be6b1-07ee-4c7f-a5e0-0208c0f73707",
    "d8e1af94-c963-4549-b53f-ba1ed435db8e",

    # Adicione mais IDs conforme necessário
]

# Intervalo em segundos entre o envio de dados para cada máquina
INTERVALO_DE_SIMULACAO_SEGUNDOS = 25

# --- Funções do Simulador ---

def simular_e_enviar_leitura(maquina_id: str):
    """
    Simula uma leitura de sensor e a envia para a API.
    Os dados simulados são similares aos que um ESP32 enviaria.
    """
    # Simula dados de sensores com variações
    leitura = {
        "id_maquina": maquina_id,
        "temperatura": round(random.uniform(75.0, 105.0), 2),  # Faixa de temperatura com picos
        "umidade": round(random.uniform(20.0, 60.0), 2),
        "vibracao_x": random.randint(2000, 4000), # Faixa de vibração com picos
        "vibracao_y": random.randint(2000, 4000),
        "vibracao_z": random.randint(2000, 4000),
        "timestamp_leitura": datetime.utcnow().isoformat()
    }

    try:
        # Envia os dados para o endpoint que adiciona a leitura no Supabase
        response = requests.post(f"{API_URL}/leituras_sensores", json=leitura)
        response.raise_for_status()  # Lança uma exceção se a resposta for um erro (ex: 404, 500)
        
        print(f"✔️ Leitura enviada para a máquina {maquina_id[:8]}... | Temp: {leitura['temperatura']}°C")

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao enviar leitura para a máquina {maquina_id[:8]}: {e}")
        # Se a API não estiver rodando, o simulador irá falhar aqui.
        # Certifique-se de que sua API Flask (app.py) está em execução.


# --- Ponto de Entrada do Script ---

if __name__ == "__main__":
    print("======================================================")
    print("🤖 INICIANDO SIMULADOR DE DADOS DE SENSORES HERMES 🤖")
    print("======================================================")
    
    if not IDS_DAS_MAQUINAS or "COLOQUE_O_ID_DA_MAQUINA_1_AQUI" in IDS_DAS_MAQUINAS:
        print("⚠️  AVISO: Por favor, configure os IDs das suas máquinas na lista 'IDS_DAS_MAQUINAS' antes de iniciar.")
    else:
        print(f"Simulando dados para {len(IDS_DAS_MAQUINAS)} máquina(s).")
        print(f"Pressione CTRL+C para parar a simulação.")
        
        try:
            # Loop infinito para simulação contínua
            while True:
                for maquina_id in IDS_DAS_MAQUINAS:
                    simular_e_enviar_leitura(maquina_id)
                    time.sleep(2) # Pequeno delay entre máquinas
                
                print(f"--- Aguardando {INTERVALO_DE_SIMULACAO_SEGUNDOS} segundos para o próximo ciclo ---")
                time.sleep(INTERVALO_DE_SIMULACAO_SEGUNDOS)

        except KeyboardInterrupt:
            print("\n✅ Simulação interrompida pelo usuário.")
            print("======================================================")