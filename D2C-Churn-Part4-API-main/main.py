from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import joblib
import pandas as pd
import os

app = FastAPI(title="D2C Churn Prediction API", version="1.0")

MODEL_PATH = "model.pkl"
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None
    print(f"Warning: Model not found at {MODEL_PATH}. Ensure it is uploaded.")

class CustomerFeatures(BaseModel):
    recency_days: int
    frequency_180d: int
    monetary_180d: float
    ticket_count_90d: int
    abandoned_carts_30d: int

class PredictionResponse(BaseModel):
    churn_probability: float
    predicted_class: int
    risk_level: str
    risk_explanation: str

def generate_explanation(prob: float, features: dict) -> str:
    if prob < 0.40:
        return "Customer shows healthy engagement metrics."
    
    reasons = []
    if features['recency_days'] > 30:
        reasons.append("slipping recency (>30 days)")
    if features['ticket_count_90d'] >= 2:
        reasons.append("elevated support ticket volume")
    if features['abandoned_carts_30d'] > 0:
        reasons.append("recent cart abandonment")
        
    base = "Elevated churn risk indicated by: "
    return base + ", ".join(reasons) if reasons else "Elevated risk based on underlying RFM pattern."

@app.get("/health")
def health_check():
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded.")
    return {"status": "ok", "message": "API is running and model is loaded."}

@app.post("/predict", response_model=PredictionResponse)
def predict_churn(customer: CustomerFeatures):
    if model is None:
        raise HTTPException(status_code=503, detail="Model is unavailable.")    
    input_data = pd.DataFrame([customer.model_dump()])
 
    prob = float(model.predict_proba(input_data)[0][1])

    pred_class = 1 if prob >= 0.40 else 0 
    
    risk_level = "high" if pred_class == 1 else "low"
    explanation = generate_explanation(prob, customer.model_dump())
    
    return {
        "churn_probability": round(prob, 4),
        "predicted_class": pred_class,
        "risk_level": risk_level,
        "risk_explanation": explanation
    }


@app.post("/batch_predict", response_model=List[PredictionResponse])
def batch_predict_churn(customers: List[CustomerFeatures]):
    responses = [predict_churn(customer) for customer in customers]
    return responses
