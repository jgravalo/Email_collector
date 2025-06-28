import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from load_data import load_data

# categorías manuales aproximadas
def asignar_categoria(texto):
    texto = texto.lower()
    if "factura" in texto:
        return "facturacion"
    elif "contrato" in texto:
        return "contrato"
    elif "baja" in texto or "cancelar" in texto:
        return "baja"
    elif "tarifa" in texto or "precio" in texto:
        return "tarifas"
    elif "suministro" in texto or "corte" in texto:
        return "incidencia"
    else:
        return "otros"

def train_model():
    emails = load_data()
    emails['categoria'] = emails['email'].apply(asignar_categoria)

    X = emails['email']
    y = emails['categoria']

    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', MultinomialNB())
    ])

    pipeline.fit(X, y)

    joblib.dump(pipeline, 'modelo.joblib')
    print("✅ Modelo entrenado y guardado en modelo.joblib")

    # exportar csv de predicciones
    predicciones = pipeline.predict(X)
    emails['prediccion'] = predicciones
    emails[['id', 'prediccion']].to_csv('predicciones.csv', index=False)

if __name__ == "__main__":
    train_model()