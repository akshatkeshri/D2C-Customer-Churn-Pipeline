from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_single_predict_success():
    payload = {
        "recency_days": 45,
        "frequency_180d": 5,
        "monetary_180d": 250.50,
        "ticket_count_90d": 2,
        "abandoned_carts_30d": 1
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "churn_probability" in data
    assert "risk_explanation" in data

def test_predict_validation_error():
    payload = {
        "recency_days": 10,
        "frequency_180d": 2,
        "ticket_count_90d": 0,
        "abandoned_carts_30d": 0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422 
