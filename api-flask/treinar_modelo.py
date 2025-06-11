# api-flask/treinar_modelo.py

import os
import pandas as pd
from dotenv import load_dotenv
from supabase import create_client, Client
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Carregar variáveis de ambiente
load_dotenv()

# --- 1. Conexão com Supabase ---
url: str = os.environ.get("SUPABASE_URL", "https://jnaosnqzjgjtkrxizyrt.supabase.co")
key: str = os.environ.get("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpuYW9zbnF6amdqdGtyeGl6eXJ0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDkwNTYwNzQsImV4cCI6MjA2NDYzMjA3NH0.MwfsUrzPfeASn_gnr4fAaQaK9wExNkovIVY6IYOYuxo")
supabase: Client = create_client(url, key)

print("Conectado ao Supabase para treinamento.")

# --- 2. Buscar Dados ---
print("Buscando dados de leituras_sensores...")
response = supabase.table('leituras_sensores').select("*").execute()
if not response.data:
    print("Nenhum dado encontrado para treinamento.")
    exit()

df = pd.DataFrame(response.data)
print(f"{len(df)} registros encontrados.")

# --- 3. Preparação e Engenharia de Features ---
print("Preparando os dados...")

# Criar feature 'vibracao_media'
df['vibracao_media'] = df[['vibracao_x', 'vibracao_y', 'vibracao_z']].mean(axis=1)

# Definir a variável alvo (target): 'failure'
# Baseado na sua arquitetura e schema,
# vamos definir uma falha quando a temperatura > 95°C ou vibração > 3000.
df['failure'] = ((df['temperatura'] > 95) | (df['vibracao_media'] > 3000)).astype(int)

# Selecionar as features para o modelo
features = ['temperatura', 'vibracao_media', 'umidade']
target = 'failure'

X = df[features]
y = df[target]

print(f"Features utilizadas: {features}")
print(f"Distribuição de falhas (1) e não-falhas (0):\n{y.value_counts()}")


# --- 4. Treinamento do Modelo RandomForestClassifier ---
print("Treinando o modelo RandomForestClassifier...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Instanciando o modelo
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')

# Treinando o modelo
model.fit(X_train, y_train)

# Avaliando o modelo (opcional, mas recomendado)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo nos dados de teste: {accuracy:.4f}")

# --- 5. Salvar o Modelo Treinado ---
model_filename = 'failure_model.pkl'
joblib.dump(model, model_filename)

print(f"✅ Modelo treinado e salvo com sucesso como '{model_filename}'!")