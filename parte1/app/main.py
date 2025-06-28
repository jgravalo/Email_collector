from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import mysql.connector

app = FastAPI()

modelo = joblib.load('modelo.joblib')

# definición de la entrada
class EmailEntrada(BaseModel):
    client_id: int
    fecha_envio: str
    email_body: str

@app.post("/classify-email")
def classify_email(data: EmailEntrada):
    # verificar si el cliente tiene impagos
    conn = mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="atc"
    )
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM impagos WHERE client_id = %s", (data.client_id,)
    )
    impagos_count = cursor.fetchone()[0]
    conn.close()

    if impagos_count > 0:
        return {
            "exito": False,
            "razon": "El cliente tiene impagos"
        }

    # si no tiene impagos, clasificamos el cuerpo
    prediccion = modelo.predict([data.email_body])[0]
    return {
        "exito": True,
        "prediccion": prediccion
    }
