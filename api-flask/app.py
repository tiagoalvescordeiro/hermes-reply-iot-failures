import os
import random
from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from supabase import create_client, Client
from dotenv import load_dotenv

# Carrega as variáveis de ambiente (se você usar um arquivo .env)
load_dotenv()

app = Flask(__name__)

# --- Configuração do Supabase ---
# As credenciais são retiradas do seu arquivo src/lib/supabaseClient.ts
url: str = os.environ.get("SUPABASE_URL", "https://jnaosnqzjgjtkrxizyrt.supabase.co")
key: str = os.environ.get("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpuYW9zbnF6amdqdGtyeGl6eXJ0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDkwNTYwNzQsImV4cCI6MjA2NDYzMjA3NH0.MwfsUrzPfeASn_gnr4fAaQaK9wExNkovIVY6IYOYuxo")
supabase: Client = create_client(url, key)

print("API conectada ao Supabase.")

# --- Endpoints da API ---

@app.route('/')
def home():
    """Endpoint principal para verificar se a API está no ar."""
    return jsonify({"status": "API do Sistema de Monitoramento Hermes Reply no ar!"}), 200

@app.route('/maquinas', methods=['POST'])
def criar_maquina():
    """
    Cria uma nova máquina.
    JSON Body: {"nome": "string", "localizacao": "string", "tipo_maquina": "string"}
    """
    data = request.get_json()
    if not data or 'nome' not in data or 'localizacao' not in data:
        return jsonify({"erro": "Dados incompletos para criar máquina."}), 400

    try:
        resultado, count = supabase.table('maquinas').insert({
            "nome": data['nome'],
            "localizacao": data['localizacao'],
            "tipo_maquina": data.get('tipo_maquina', 'industrial'),
            "status_operacional": "ativo"
        }).execute()
        return jsonify({"mensagem": "Máquina criada com sucesso!", "dados": resultado[1]}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/leituras_sensores', methods=['POST'])
def adicionar_leitura():
    """
    Adiciona uma nova leitura de sensor para uma máquina específica.
    JSON Body: {"id_maquina": "uuid"}
    """
    data = request.get_json()
    if not data or 'id_maquina' not in data:
        return jsonify({"erro": "O ID da máquina é obrigatório."}), 400

    # Simula dados de sensores, como faria o ESP32
    leitura = {
        "id_maquina": data['id_maquina'],
        "temperatura": round(random.uniform(75.0, 105.0), 2),  # Simula temperaturas mais altas
        "umidade": round(random.uniform(20.0, 60.0), 2),
        "vibracao_x": random.randint(2000, 4000), # Simula vibrações mais altas
        "vibracao_y": random.randint(2000, 4000),
        "vibracao_z": random.randint(2000, 4000),
        "timestamp_leitura": datetime.utcnow().isoformat()
    }

    try:
        resultado, count = supabase.table('leituras_sensores').insert(leitura).execute()
        return jsonify({"mensagem": "Leitura de sensor adicionada!", "dados": resultado[1]}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/alertas', methods=['POST'])
def criar_alerta():
    """
    Cria um novo alerta para uma máquina.
    JSON Body: {"id_maquina": "uuid", "tipo_alerta": "string", "severidade": "string", ...}
    """
    data = request.get_json()
    # Validação básica
    required_fields = ['id_maquina', 'tipo_alerta', 'severidade', 'titulo', 'descricao']
    if not all(field in data for field in required_fields):
        return jsonify({"erro": f"Campos obrigatórios ausentes: {required_fields}"}), 400

    try:
        resultado, count = supabase.table('alertas').insert(data).execute()
        return jsonify({"mensagem": "Alerta criado com sucesso!", "dados": resultado[1]}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/configuracoes_limites', methods=['POST'])
def configurar_limite():
    """
    Configura os limites de um sensor para uma máquina.
    JSON Body: {"id_maquina": "uuid", "tipo_sensor": "string", "limite_warning": float, ...}
    """
    data = request.get_json()
    required_fields = ['id_maquina', 'tipo_sensor', 'limite_warning', 'limite_critical', 'unidade']
    if not all(field in data for field in required_fields):
        return jsonify({"erro": f"Campos obrigatórios ausentes: {required_fields}"}), 400

    try:
        # Upsert para criar ou atualizar a configuração
        resultado, count = supabase.table('configuracoes_limites').upsert(data).execute()
        return jsonify({"mensagem": "Configuração de limite salva!", "dados": resultado[1]}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/manutencoes', methods=['POST'])
def agendar_manutencao():
    """
    Agenda ou registra uma manutenção.
    JSON Body: {"id_maquina": "uuid", "tipo_manutencao": "string", "descricao": "string", ...}
    """
    data = request.get_json()
    required_fields = ['id_maquina', 'tipo_manutencao', 'descricao', 'data_inicio']
    if not all(field in data for field in required_fields):
        return jsonify({"erro": f"Campos obrigatórios ausentes: {required_fields}"}), 400

    try:
        resultado, count = supabase.table('manutencoes').insert(data).execute()
        return jsonify({"mensagem": "Manutenção registrada!", "dados": resultado[1]}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


if __name__ == '__main__':
    # A porta padrão do Flask é 5000
    app.run(debug=True, port=5000)