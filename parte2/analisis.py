import pandas as pd
import requests
from sqlalchemy import create_engine

# conectar a MySQL
engine = create_engine("mysql+pymysql://root:root@localhost:3306/atc")
df = pd.read_sql("SELECT id, client_id, fecha_envio, email FROM emails", con=engine)

# convertir fechas
df['fecha_envio'] = pd.to_datetime(df['fecha_envio'], errors='coerce')

# clasificar cada email llamando a la API
categorias = []
for idx, row in df.iterrows():
    try:
        response = requests.post(
            "http://localhost:8000/classify-email",
            json={
                "client_id": int(row["client_id"]),
                "fecha_envio": str(row["fecha_envio"]),
                "email_body": row["email"]
                }
        )
        response.raise_for_status()
        categorias.append(response.json()["prediccion"])
    except Exception as e:
        # print(f"Error clasificando id={row['id']}: {e}")
        categorias.append("cliente con impagos")

df["categoria"] = categorias

# volumen por categoría
print("\n=== Volumen de correos por categoría ===")
print(df['categoria'].value_counts())

# distribución temporal por mes
df['mes'] = df['fecha_envio'].dt.to_period('M')
print("\n=== Distribución temporal de correos por mes ===")
print(df.groupby(['mes']).size())
print("\n=== Distribución temporal de correos por categoría (mensual) ===")
print(df.groupby(['mes', 'categoria']).size())

# distribución por día de la semana
df['dia_semana'] = df['fecha_envio'].dt.day_name()
print("\n=== Distribución de correos por día de la semana ===")
print(df.groupby(['dia_semana']).size())
print("\n=== Distribución de correos por categoría (diaria) ===")
print(df.groupby(['dia_semana', 'categoria']).size())
