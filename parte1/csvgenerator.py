import pandas as pd
import mysql.connector
import requests
import time

# conecta a la base de datos
conn = mysql.connector.connect(
    # host="db",  # servicio docker
	host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="atc"
)

emails_df = pd.read_sql("SELECT * FROM emails", conn)
conn.close()

resultados = []

for idx, row in emails_df.iterrows():
    payload = {
        "client_id": int(row["client_id"]),
        "fecha_envio": str(row["fecha_envio"]),
        "email_body": row["email"]
    }
    try:
        response = requests.post("http://localhost:8000/classify-email", json=payload)
        if response.status_code == 200:
            data = response.json()
            if data.get("exito"):
                pred = data.get("prediccion")
            else:
                pred = "cliente_con_impagos"
            resultados.append({
                "id_email": row["id"],
                "prediccion": pred,
				# test de datos
                # "client_id": int(row["client_id"]),
                # "fecha_envio": str(row["fecha_envio"]),
                #email_body": row["email"]
            })
        else:
            print(f"Error en fila id {row['id']}, status {response.status_code}")
            resultados.append({
                "id_email": row["id"],
                "prediccion": "error"
            })
    except Exception as e:
        print(f"Error con email id {row['id']}: {e}")
        resultados.append({
            "id_email": row["id"],
            "prediccion": "error"
        })
    
    # un pequeño delay para no saturar la api
    time.sleep(0.1)

# guardamos CSV
df_resultados = pd.DataFrame(resultados)
df_resultados.to_csv("categorias.csv", index=False)
print("Archivo categorias.csv generado.")