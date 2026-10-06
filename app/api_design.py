from pathlib import Path

import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from schema.schema import SalaryPredictionInput
from schema.transformer import transform_input


# =========================================================
# PATHS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "salary_prediction_model.pkl"


# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load(MODEL_PATH)


# =========================================================
# FASTAPI APP
# =========================================================

app = FastAPI(
    title="AI Salary Prediction API",
    description="API for predicting AI/ML job salaries",
    version="1.0.0"
)


# =========================================================
# RESPONSE SCHEMA
# =========================================================

class SalaryPredictionResponse(BaseModel):

    predicted_salary_usd: float


# =========================================================
# HOME
# =========================================================

@app.get("/")
def home():

    return {
        "message": "AI Salary Prediction API is running"
    }


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }


# =========================================================
# PREDICTION
# =========================================================

@app.post(
    "/predict",
    response_model=SalaryPredictionResponse
)
def predict(data: SalaryPredictionInput):

    model_input = transform_input(data)

    prediction = model.predict(model_input)

    return {
        "predicted_salary_usd": round(
            float(prediction[0]),
            2
        )
    }