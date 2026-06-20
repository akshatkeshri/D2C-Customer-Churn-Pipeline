# Edge-Case Manual Review Log

## Objective
Machine learning models and rigid RFM rules cannot capture every nuance of human behavior. The following 10 customers were isolated via an automated query because their data presents a conflicting "edge case" requiring manual review by the marketing or product team.

## Isolation Logic
These users were flagged because they exhibit the following contradictory signals:
1. **Above Average Spend:** Their `monetary_180d` is higher than the dataset median.
2. **Slipping Recency:** They have not made a purchase in over 30 days.
3. **High Current Intent:** Despite not buying recently, they are aggressively browsing the site (5 or more sessions in the last 30 days).

They are window shopping heavily but failing to convert.

## The 10 Flagged Customer IDs

| Customer ID | Assigned Segment | Recency (Days) | 180-Day Spend | 30-Day Sessions |
| :--- | :--- | :--- | :--- | :--- |
| **CUST00005** | Champions | 38 | 1781.90 | 18 |
| **CUST00014** | Champions | 51 | 1382.39 | 11 |
| **CUST00015** | Champions | 35 | 1523.14 | 6 |
| **CUST00026** | At-Risk Customers | 72 | 3561.39 | 14 |
| **CUST00027** | Discount-Sensitive | 70 | 2128.34 | 11 |
| **CUST00034** | Champions | 50 | 1460.21 | 7 |
| **CUST00038** | Champions | 51 | 1955.61 | 5 |
| **CUST00048** | Champions | 61 | 2450.45 | 12 |
| **CUST00052** | Champions | 55 | 1820.53 | 7 |
| **CUST00057** | Loyal Customers | 136 | 1713.34 | 7 |

## Required Manual Action & Reasoning
A simple discount might not fix whatever is stopping these specific high-value users from checking out. 

**Recommended Action:** The UX/Product team should manually review the session recordings or click-paths for these 10 individuals (particularly `CUST00005`, who logged a massive 18 sessions without buying). 

**Hypotheses to investigate:**
* Is there a technical bug on their preferred device preventing checkout?
* Are the specific items they keep viewing chronically out of stock?
* Are shipping costs to their specific region causing them to abandon their journey at the last minute? 

Understanding the friction points for these 10 highly motivated shoppers will likely uncover systemic issues affecting the broader user base.
