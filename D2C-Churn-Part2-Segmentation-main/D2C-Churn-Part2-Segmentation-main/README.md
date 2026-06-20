# Part 2: RFM Segmentation & Retention Strategy

## Project Overview
This repository contains Part 2 of the D2C customer churn capstone. The objective is to build a rule-based customer segmentation engine prior to deploying machine learning models. It utilizes Recency, Frequency, and Monetary (RFM) modeling, combined with non-RFM behavioral signals (support ticket volume and web session data), to isolate distinct customer cohorts and recommend targeted, budget-efficient retention actions.

## Repository Contents
* `rfm_segmentation.ipynb`: The core notebook detailing feature engineering and segmentation logic.
* `segments.csv`: The final dataset mapping each `customer_id` to its assigned segment and underlying features.
* `retention_strategy.md`: A business strategy document defining segment behaviors and recommended marketing actions.
* `manual_review_cases.md`: An analysis of 10 edge-case customers requiring human-in-the-loop intervention.
* `requirements.txt`: Python dependencies.

## How to Run This Project
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `/data` folder in the root directory.
4. Add `rfm_modeling_snapshot.csv`, `support_tickets.csv`, and `web_events_snapshot.csv` to the `/data` folder.
5. Execute all cells in `rfm_segmentation.ipynb`.
