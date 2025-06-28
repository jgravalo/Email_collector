import pandas as pd
import mysql.connector
import time

def load_data():
	print('Conectando a la base de datos...')
	for i in range(30):
		try:
			conn = mysql.connector.connect(
				host="db",
				user="root",
				password="root",
				database="atc"
			)
			break
		except mysql.connector.Error as e:
			print(f"Intento {i+1}: Esperando a que MySQL esté listo... ({e})")
			time.sleep(4)
	else:
		raise Exception("No se pudo conectar a MySQL después de varios intentos.")
	print('Conexión exitosa a la base de datos.')

	cursor = conn.cursor()
	cursor.execute("SELECT COUNT(*) FROM clientes;")
	result = cursor.fetchone()
	print(f"Número de clientes: {result[0]}")
	cursor.close()

	clientes = pd.read_sql("SELECT * FROM clientes", conn)
	emails = pd.read_sql("SELECT * FROM emails", conn)
	impagos = pd.read_sql("SELECT client_id FROM impagos", conn)

	# filtrar emails de clientes morosos
	emails_filtrados = emails[~emails['client_id'].isin(impagos['client_id'])]

	print(f"Total de emails filtrados: {len(emails_filtrados)}")
	# emails_filtrados.to_csv('emails_filtrados.csv', index=False)

	conn.close()
	return emails_filtrados