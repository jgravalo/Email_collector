from datetime import datetime


def main() -> None:
    # Debería responder indicando que puede descargar su última factura desde la app o el área clientes.
    id_cliente = 123
    fecha_envio = datetime.now()
    email_body = "Hola, quiero una copia de mi última factura."

    email_category = ...  # Obtener la categoría del email usando la API de la parte 1
    reply = ...  # Generar la respuesta usando la API de OpenAI, teniendo en cuenta la categoría y el cuerpo del correo
    print(reply)


if __name__ == "__main__":
    main()
