# Data Quality Report

## Overview
This report details the data quality audit conducted on the raw D2C customer datasets prior to exploratory data analysis and predictive modeling. The audit ensures structural integrity and strict adherence to the evaluation snapshot date of `2025-09-30`.

## 1. Dataset Dimensions & Completeness
The dataset encompasses a base of 2,400 unique customers. Across all tables, zero exact duplicate rows were detected.

* **Customers:** 2,400 rows
* **Orders:** 8,137 rows
* **Support Tickets:** 1,921 rows
* **Web Events:** 2,400 rows
* **Interventions:** 2,400 rows
* **Churn Labels:** 2,400 rows

## 2. Missing Values Analysis
Missing data was identified in two primary tables:

**A. Customers Table (`customers.csv`)**
* **`loyalty_tier` (1,386 missing / 57.75%):** A critical absence. Over half the customer base lacks an assigned loyalty tier. 
    * *Handling Strategy:* These rows cannot be dropped due to the high volume. The missing status likely represents a distinct behavioral segment (e.g., guest checkouts, inactive users, or incomplete profile onboarding). This null state will be encoded as a distinct category (e.g., "Unassigned") for feature engineering.
* **`skin_type` (401 missing / 16.71%):** * *Handling Strategy:* Similar to loyalty tier, a missing skin profile suggests lower engagement with the brand's personalization features. This will be imputed as "Unknown."

**B. Orders Table (`orders.csv`)**
* **`rating` (58 missing / 0.71%):**
    * *Handling Strategy:* Given the low percentage, these missing ratings can either be imputed with the median rating or flagged as "Unrated," as the act of not leaving a rating may carry predictive weight regarding customer engagement.

## 3. Data Leakage & Date Consistency Prevention
To ensure the integrity of the downstream predictive model, a strict temporal boundary was enforced using the provided snapshot date of `2025-09-30`.

* **Transactional Filtering:** The `orders.csv` and `support_tickets.csv` tables contain granular timestamp data (`order_date` and `ticket_date`). An automated filter was applied during data loading to systematically drop any records occurring after `2025-09-30`.
* **Pre-Aggregated Datasets:** Schema inspection revealed that `web_events_snapshot.csv` and `intervention_history.csv` do not contain granular event dates, but rather a uniform `snapshot_date` column. These tables represent behavior pre-aggregated up to the cutoff point, requiring no further row-level temporal filtering.

## 4. Join/Key Integrity
All secondary tables (`orders`, `support_tickets`, `web_events`, `interventions`, `churn_labels`) successfully map back to the primary `customers` table via the `customer_id` primary key. The row counts for the aggregated tables (2,400 rows each) match the total unique customer count perfectly, indicating a 1:1 relationship and clean referential integrity across the snapshot.
