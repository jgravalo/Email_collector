FROM python:3.9

WORKDIR /app

## CONTINUAR AQUÍ
COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# Ejecuta el script de limpieza antes de arrancar la app
# RUN python parse_sql.py

# CMD ["python", "main.py"]


EXPOSE 8000

CMD ["bash", "-c", "python train_model.py && uvicorn main:app --host 0.0.0.0 --port 8000"]