from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.linear_model import LinearRegression
import numpy as np
import os # DODANO: Import biblioteki do zmiennych środowiskowych

app = FastAPI(title="ML API Laboratorium 05")

X_train = np.array([[1.0], [2.0], [3.0], [4.0]])
y_train = np.array([3.0, 5.0, 7.0, 9.0])
model = LinearRegression()
model.fit(X_train, y_train)

class PredictRequest(BaseModel):
    feature_x: float

@app.get("/")
def read_root():
    return {"message": "Witaj w API model ML - Serverless!"}

@app.post("/predict")
def predict(data: PredictRequest):
    try:
        prediction = model.predict([[data.feature_x]])
        return {"prediction": float(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Błąd podczas predykcji: {str(e)}")

@app.get("/info")
def get_info():
    # DODANO: Pobieranie zmiennej środowiskowej
    app_version = os.getenv("APP_VERSION", "Wersja domyślna (brak zmiennej)")
    return {
        "model_type": "LinearRegression",
        "wersja_aplikacji": app_version
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}