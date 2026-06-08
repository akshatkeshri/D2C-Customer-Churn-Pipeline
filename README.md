# 🚀 D2C Customer Churn Prediction & Retention Pipeline

## Executive Summary
This project is an end-to-end machine learning and data engineering capstone designed to solve a critical business problem for a Direct-to-Consumer (D2C) personal-care brand: **a 47% baseline customer churn rate.** Rather than relying on blanket discounts that erode profit margins, this pipeline transitions the business to a targeted, data-driven retention strategy. It spans the entire data lifecycle—from raw exploratory data analysis and rule-based Recency, Frequency, Monetary (RFM) segmentation, to training an XGBoost predictive model and deploying it as a real-time FastAPI microservice.

---

## 🏗️ The Machine Learning Pipeline (Project Architecture)
This architecture is modularized into four distinct phases. Click into any phase below to view the specific code, documentation, and business strategies associated with it.

### 📊 [Phase 1: Exploratory Data Analysis & Quality Audit](https://github.com/akshatkeshri/D2C-Churn-Part1-EDA)
* **Objective:** Clean raw CRM/Web event data and identify baseline churn behavioral indicators.
* **Key Findings:** Discovered the "Silent User" paradox—churn is driven by digital apathy (lack of web sessions) rather than negative experiences (support tickets or returns).
* **Highlights:** Data Quality Report, Missing Value Imputation, Visual Distribution Analysis.

### 🎯 [Phase 2: RFM Customer Segmentation](https://github.com/akshatkeshri/D2C-Churn-Part2-Segmentation)
* **Objective:** Build a rule-based customer tiering engine to isolate high-value risk groups.
* **Key Findings:** Segmented the 2,400 user base into 6 distinct cohorts. Identified exactly 369 high-value users ("At-Risk" and "High-Value but Unhappy") where retention marketing budget should be aggressively prioritized.
* **Highlights:** Quantile Scoring, Edge-Case Manual Review, Budget Prioritization Strategy.

### 🧠 [Phase 3: Predictive Modeling (XGBoost)](https://github.com/akshatkeshri/D2C-Churn-Part3-Prediction)
* **Objective:** Train a machine learning classifier to predict 60-day churn likelihood based on the RFM and web-behavior snapshot.
* **Key Findings:** Tuned the probability decision threshold from the default `0.50` down to `0.40` to prioritize catching churners. Achieved an **82% Recall** for the churn class (successfully identifying 82 out of every 100 churning customers).
* **Highlights:** Feature Engineering, Leakage Prevention, Threshold Tuning, False Positive/Negative Business Impact Analysis.

### 🚀 [Phase 4: API Deployment & Software Engineering](https://github.com/akshatkeshri/D2C-Churn-Part4-API)
* **Objective:** Wrap the serialized XGBoost model into a production-ready microservice for real-time CRM integration.
* **Key Findings:** Engineered a scalable API capable of evaluating customer data payloads and returning probability scores alongside human-readable risk explanations.
* **Highlights:** FastAPI, Pydantic Data Validation, Automated Pytest Suite, Dockerization, Swagger UI.

---

## 🛠️ Technology Stack
* **Languages:** Python 3.10+
* **Data Processing & EDA:** Pandas, NumPy, Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn, XGBoost
* **Deployment & Software Engineering:** FastAPI, Uvicorn, Pytest, Docker, Pydantic

---

## 📈 Business Impact
By deploying this pipeline, the D2C brand can transition from a reactive, mass-discounting model to a proactive, predictive model. Identifying at-risk customers with an 82% recall rate before their 60-day churn window closes allows for highly personalized interventions, ultimately increasing Customer Lifetime Value (CLTV) and maximizing marketing ROI.
