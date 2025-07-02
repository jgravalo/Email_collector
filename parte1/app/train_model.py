import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from load_data import load_data
import re

# categorías manuales aproximadas
def asignar_categoria(texto):
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)  # elimina signos de puntuación

    # diccionario de categorias -> lista de palabras clave
    categorias = {
        "facturacion": ["factura", "historial"],
        "contrato": ["contrato", "datos"],
        "altas y bajas": ["contratar", "alta", "baja", "cancelar"],
        "tarifas": ["tarifa", "precio", "descuento", "oferta", "promocion", "plan"],
        "incidencia": ["suministro", "corte", "asistencia", "problema"],
    }

    for categoria, palabras in categorias.items():
        if any(p in texto for p in palabras):
            return categoria

    return "otros"


def train_model():
    emails = load_data()
    emails['categoria'] = emails['email'].apply(asignar_categoria)
    for idx, email in emails.iterrows():
        print(f"({email['categoria']}); {email['email']})")
        # print(f"{email['id']}: ({email['categoria']}); {email['email']})")

    """
    for categoria, cantidad in emails['categoria'].value_counts().items():
        print(f"Categoría: {categoria}, Cantidad: {cantidad}")
    """
    X = emails['email']
    y = emails['categoria']

    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', MultinomialNB())
    ])

    pipeline.fit(X, y)

    joblib.dump(pipeline, 'modelo.joblib')
    print("Modelo entrenado y guardado en modelo.joblib")

    # exportar csv de predicciones
    predicciones = pipeline.predict(X)
    emails['prediccion'] = predicciones
    emails[['id', 'prediccion']].to_csv('predicciones.csv', index=False)

if __name__ == "__main__":
    train_model()
