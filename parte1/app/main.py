import mysql.connector
import time

def main():
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
	conn.close()

if __name__ == "__main__":
	main()