FROM python:3.9

WORKDIR /app

## CONTINUAR AQUÍ
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ejecuta el script de limpieza antes de arrancar la app
# RUN python parse_sql.py

CMD ["python", "main.py"]