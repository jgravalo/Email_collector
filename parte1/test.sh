curl -X POST http://localhost:8000/classify-email \
  -H "Content-Type: application/json" \
  -d '{
    "client_id": 3,
    "fecha_envio": "2024-01-01 10:00:00",
    "email_body": "Hola, quiero ver mi factura"
  }'
echo
curl -X POST http://localhost:8000/classify-email \
  -H "Content-Type: application/json" \
  -d '{
    "client_id": 3,
    "fecha_envio": "2022-11-09 20:40:38",
    "email_body": "Hola buenas tardes, necesito que me envíen el contrato de electricidad y gas. Nunca me lo han enviado"
  }'
echo
curl -X POST http://localhost:8000/classify-email \
  -H "Content-Type: application/json" \
  -d '{
    "client_id": 4,
    "fecha_envio": "2022-04-18 07:11:29",
    "email_body": "Hola, yo llamaba porque quiero darme de baja del servicio de gas. Entonces parece que he llegado un poco tarde, por eso es las seis y media. El teléfono mío es 6666666666. Si puede mañana me llamo. Gracias."
  }'
echo