# Post-Deployment Monitoring Plan

To ensure the API remains reliable and the predictions remain accurate over time, the following metrics will be tracked:

## 1. Data Drift
* Track the incoming distributions of core features (especially `recency_days` and `monetary_180d`) via the API logs. 
* Compare weekly averages against the original training dataset (Snapshot: 2025-09-30). Significant deviation indicates the business environment has changed.

## 2. Prediction Distribution
* Monitor the ratio of predicted classes. If the model suddenly flags 80% of all traffic as "high risk" (class 1), an alert should trigger to investigate potential upstream data pipeline bugs.

## 3. Business Outcomes
* Implement a feedback loop linking the API predictions back to the CRM database.
* Track the actual 60-day retention rate of customers flagged as "high risk" who received a marketing intervention vs. those who did not.

## 4. API Errors & Latency
* Monitor HTTP 422 (Validation Errors) to ensure upstream systems are formatting the JSON payloads correctly.
* Track P99 latency to ensure predictions are returned in under 200ms to avoid bottlenecking the CRM tool.

## 5. Retraining Triggers
* **Temporal:** Retrain the model quarterly to capture new seasonal trends.
* **Performance-based:** Retrain immediately if the Precision metric in the live feedback loop drops below 65%.
