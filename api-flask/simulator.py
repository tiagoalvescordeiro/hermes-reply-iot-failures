import requests
import random
import time
from datetime import datetime, timedelta

# URL base da nossa API Flask que está rodando localmente
API_URL = "http://127.0.0.1:5000"

# --- Dados Fictícios para Simulação ---

MAQUINAS_A_CRIAR = [
    {"nome": "Prensa Hidráulica PH-300", "localizacao": "Setor de Prensagem", "tipo_maquina": "Prensa"},
    {"nome": "Torno CNC T-2500", "localizacao": "Setor de Usinagem", "tipo_maquina": "CNC"},
    {"nome": "Esteira de Montagem EM-A5", "localizacao": "Linha de Montagem A", "tipo_maquina": "Esteira"},
    {"nome": "Robô de Solda RS-808", "localizacao": "Célula de Soldagem 2", "tipo_maquina": "Robô"}
]

TIPOS_ALERTA = {
    "temperatura": {"titulo": "Temperatura Elevada", "descricao": "Temperatura excedeu o limite de segurança.", "severidade_opts": ["warning", "critical"]},
    "vibracao": {"titulo": "Vibração Anormal", "descricao": "Níveis de vibração anormais detectados.", "severidade_opts": ["warning", "critical"]},
    "sistema": {"titulo": "Falha no Sistema", "descricao": "Um componente do sistema reportou um erro.", "severidade_opts": ["info", "warning"]}
}

TIPOS_MANUTENCAO = ["preventiva", "corretiva", "preditiva"]
STATUS_MANUTENCAO = ["agendada", "em_andamento", "concluida"]
TECNICOS = ["Carlos Silva", "Mariana Costa", "Roberto Alves", "Ana Pereira"]

# --- Funções para Interagir com a API ---

def criar_maquinas():
    """Cria as 4 máquinas iniciais e retorna seus IDs."""
    ids_maquinas = []
    print("--- 1. Criando Máquinas ---")
    for maquina in MAQUINAS_A_CRIAR:
        try:
            response = requests.post(f"{API_URL}/maquinas", json=maquina)
            response.raise_for_status()  # Lança exceção para respostas de erro (4xx ou 5xx)
            
            dados = response.json()
            novo_id = dados['dados'][0]['id']
            ids_maquinas.append(novo_id)
            print(f"✔️ Máquina '{maquina['nome']}' criada com sucesso. ID: {novo_id}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao criar máquina '{maquina['nome']}': {e}")
            print(f"   Resposta do servidor: {e.response.text if e.response else 'N/A'}")
            
    return ids_maquinas

def simular_leituras_de_sensores(ids_maquinas, num_leituras_por_maquina=10):
    """Simula e envia leituras de sensores para cada máquina."""
    print(f"\n--- 2. Simulando {num_leituras_por_maquina} Leituras de Sensores por Máquina ---")
    for maquina_id in ids_maquinas:
        print(f"  > Enviando dados para a máquina {maquina_id[:8]}...")
        for i in range(num_leituras_por_maquina):
            try:
                response = requests.post(f"{API_URL}/leituras_sensores", json={"id_maquina": maquina_id})
                response.raise_for_status()
                # print(f"    Leitura {i+1}/{num_leituras_por_maquina} enviada.")
            except requests.exceptions.RequestException as e:
                print(f"❌ Erro ao enviar leitura para {maquina_id[:8]}: {e.response.text}")
            time.sleep(0.1) # Pequeno delay para não sobrecarregar a API
    print("✔️ Leituras de sensores simuladas com sucesso!")

def configurar_limites(ids_maquinas):
    """Configura limites padrão para os sensores de cada máquina."""
    print("\n--- 3. Configurando Limites dos Sensores ---")
    for maquina_id in ids_maquinas:
        configs = [
            {"tipo_sensor": "temperatura", "limite_warning": 85.0, "limite_critical": 95.0, "unidade": "°C"},
            {"tipo_sensor": "vibracao", "limite_warning": 3000, "limite_critical": 3500, "unidade": "Hz"},
            {"tipo_sensor": "umidade", "limite_warning": 60.0, "limite_critical": 70.0, "unidade": "%"}
        ]
        for config in configs:
            payload = {"id_maquina": maquina_id, **config}
            try:
                response = requests.post(f"{API_URL}/configuracoes_limites", json=payload)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"❌ Erro ao configurar limite para {maquina_id[:8]}: {e.response.text}")
    print(f"✔️ Limites configurados para {len(ids_maquinas)} máquinas.")
    
def simular_alertas(ids_maquinas, chance_alerta=0.4):
    """Simula a criação de alertas para algumas máquinas."""
    print("\n--- 4. Simulando Alertas ---")
    for maquina_id in ids_maquinas:
        if random.random() < chance_alerta:
            tipo = random.choice(list(TIPOS_ALERTA.keys()))
            detalhes = TIPOS_ALERTA[tipo]
            severidade = random.choice(detalhes["severidade_opts"])
            
            alerta = {
                "id_maquina": maquina_id,
                "tipo_alerta": tipo,
                "severidade": severidade,
                "titulo": detalhes["titulo"],
                "descricao": detalhes["descricao"],
                "valor_sensor": round(random.uniform(90.0, 110.0), 2) if tipo == 'temperatura' else random.randint(3200, 4000),
                "threshold_valor": 85.0 if severidade == "warning" else 95.0,
                "resolvido": False
            }
            try:
                response = requests.post(f"{API_URL}/alertas", json=alerta)
                response.raise_for_status()
                print(f"  > 🚨 Alerta '{severidade}' criado para a máquina {maquina_id[:8]}")
            except requests.exceptions.RequestException as e:
                 print(f"❌ Erro ao criar alerta para {maquina_id[:8]}: {e.response.text}")

def simular_manutencoes(ids_maquinas, chance_manutencao=0.6):
    """Simula o registro de manutenções para algumas máquinas."""
    print("\n--- 5. Registrando Manutenções ---")
    for maquina_id in ids_maquinas:
        if random.random() < chance_manutencao:
            data_inicio = datetime.utcnow() - timedelta(days=random.randint(1, 30))
            manutencao = {
                "id_maquina": maquina_id,
                "tipo_manutencao": random.choice(TIPOS_MANUTENCAO),
                "descricao": f"Manutenção de rotina no sistema {random.choice(['hidráulico', 'elétrico', 'mecânico'])}.",
                "tecnico_responsavel": random.choice(TECNICOS),
                "data_inicio": data_inicio.isoformat(),
                "data_fim": (data_inicio + timedelta(hours=random.randint(2,8))).isoformat(),
                "custo": round(random.uniform(500.0, 5000.0), 2),
                "status_manutencao": "concluida"
            }
            try:
                response = requests.post(f"{API_URL}/manutencoes", json=manutencao)
                response.raise_for_status()
                print(f"  > 🔧 Manutenção registrada para a máquina {maquina_id[:8]}")
            except requests.exceptions.RequestException as e:
                print(f"❌ Erro ao registrar manutenção para {maquina_id[:8]}: {e.response.text}")
                
if __name__ == "__main__":
    print("======================================================")
    print("🤖 INICIANDO SIMULADOR DE DADOS INDUSTRIAIS HERMES 🤖")
    print("======================================================")
    
    # Executa a cadeia de simulação
    ids_das_maquinas = criar_maquinas()
    
    if ids_das_maquinas:
        configurar_limites(ids_das_maquinas)
        simular_leituras_de_sensores(ids_das_maquinas, num_leituras_por_maquina=15)
        simular_alertas(ids_das_maquinas)
        simular_manutencoes(ids_das_maquinas)
    else:
        print("\nNenhuma máquina foi criada. O simulador não pode continuar.")

    print("\n✅ Simulação concluída! Verifique seu dashboard e o banco Supabase.")
    print("======================================================")