import mysql.connector

def main():
	print('Conectando a la base de datos...')
		""" conn = mysql.connector.connect(
			host="db",      # Cambia si tu host es diferente
			user="root",    # Cambia por tu usuario
			password="tu_password",  # Cambia por tu contraseña
			database="atc"
		)
		cursor = conn.cursor()
		cursor.execute("SELECT COUNT(*) FROM clientes;")
		result = cursor.fetchone()
		print(f"Número de clientes: {result[0]}")
		cursor.close()
		conn.close() """

	if __name__ == "__main__":
		main()