from datetime import datetime
import requests
from openai import OpenAI

def main() -> None:
    # Datos de prueba
    id_cliente = 123
    fecha_envio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    email_body = "Hola, quiero una copia de mi última factura."
    # email_body = "Hola, se me ha cortado el gas."
    # email_body = "Hola, quiero dar de baja mi contrato con la empresa."

    # leer la apikey
    with open("apikey.txt") as f:
        openai_api_key = f.read().strip()

    # inicializar cliente GPT
    client = OpenAI(api_key=openai_api_key)

    # ===== Paso 1: clasificar el correo con la API de la parte 1 =====
    try:
        response = requests.post(
            "http://localhost:8000/classify-email",
            json={
                "client_id": id_cliente,
                "fecha_envio": fecha_envio,
                "email_body": email_body
            },
            timeout=5
        )
        response.raise_for_status()
    except Exception as e:
        print(f"Error llamando a la API de clasificación: {e}")
        return

    data = response.json()
    if not data.get("exito", True):
        print(f"Cliente con impagos o error: {data.get('razon')}")
        return

    email_category = data.get("prediccion", "otros")
    print(f"Categoría detectada: {email_category}")

    # ===== Paso 2: generación de respuesta con GPT =====
    ejemplos = {
        "facturacion": "Buenas tardes, gracias por su consulta. Puede encontrar y descargar todas sus facturas en el área de clientes de nuestra web o en la aplicación móvil.",
        "contrato": "Buenas tardes, gracias por su consulta. Puede descargar su contrato desde el área de clientes o contactarnos para recibirlo por correo electrónico.",
        "tarifas": "Hola, gracias por su interés. Todas nuestras tarifas y promociones actualizadas están disponibles en nuestra página web de Factor Energía.",
        "incidencia": "Hola, gracias por contactarnos. Un agente revisará el problema de suministro que indica tan pronto como sea posible y se pondrá en contacto con usted.",
        "baja": "Lamentamos que quiera darse de baja. Para tramitarlo, por favor contacte con nuestro equipo de atención llamando al 900 123 456, o a través del área de clientes."
    }

    if email_category in ejemplos:
        system_prompt = f"""Eres un agente de atención al cliente de Factor Energía. Responde con un estilo amable, breve y claro, en español. Toma como referencia este ejemplo de respuesta corporativa:

{ejemplos[email_category]}

Personaliza la respuesta basándote en el siguiente correo recibido:"""

        user_prompt = email_body

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        reply = completion.choices[0].message.content
    else:
        # Respuesta por defecto
        reply = "Gracias por su mensaje. Un agente revisará su consulta y se pondrá en contacto con usted lo antes posible."

    # Mostrar el borrador
    print("\n===== BORRADOR DE RESPUESTA =====")
    print(reply)


if __name__ == "__main__":
    main()
