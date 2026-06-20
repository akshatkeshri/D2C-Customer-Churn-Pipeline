# Responsible Use Guidelines for Retention Team

This API provides probability scores regarding customer churn. It is a probabilistic tool, not an absolute certainty.

## How to use the API output:
* **Prioritize Workflows:** Use the `predicted_class` to prioritize manual outreach queues for Customer Success agents.
* **A/B Testing:** Use the `risk_level` to test different retention offers (e.g., offering High-Risk users a 20% discount, while offering Low-Risk users early product access).

## How NOT to use the API output:
* **Denying Service:** The model must never be used to deny returns, restrict support access, or penalize customers flagged as high risk.
* **Blind Automation:** Do not blindly automate massive financial incentives solely based on the `churn_probability` score without budgetary caps, as False Positives are an expected part of the model's behavior.
