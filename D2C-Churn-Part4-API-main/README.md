# Part 4: FastAPI Churn Scoring Service

## Project Overview
This repository contains the deployment phase of the D2C customer churn capstone. It provides a production-ready FastAPI web service that loads a serialized machine learning model and serves real-time churn predictions for integration with an internal CRM.

## Setup Instructions & Installation
1. Clone the repository.
2. Ensure you have Python 3.9+ installed.
3. Install dependencies:
   `pip install -r requirements.txt`
4. Ensure the `model.pkl` file (from Part 3) is located in the root directory.

## Command to Run the API
To start the development server, execute the following command in your terminal:
`uvicorn main:app --reload`

## Endpoint Details
* `GET /health`: Verifies the API is running and the `.pkl` model has successfully loaded into memory.
* `POST /predict`: Accepts a single customer JSON payload, validates the datatypes using Pydantic, and returns a churn prediction and risk explanation.
* `POST /batch_predict`: Accepts a list of customer JSON payloads for bulk processing.

## Sample Request (`POST /predict`)
```json
{
  "recency_days": 45,
  "frequency_180d": 3,
  "monetary_180d": 150.00,
  "ticket_count_90d": 2,
  "abandoned_carts_30d": 1
}
