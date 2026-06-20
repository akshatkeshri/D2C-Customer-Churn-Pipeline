# Business Memo: Phase 1 Exploratory Data Analysis
**To:** Product & Marketing Teams
**Subject:** Initial Findings on Customer Churn & Engagement Apathy

## Executive Summary
Following a comprehensive audit of our user snapshot (as of 2025-09-30), we have identified an overall baseline churn rate of **46.96%**. 

Initial exploratory data analysis reveals a counter-intuitive pattern: customer churn is not primarily driven by high-friction negative experiences (like excessive returns or customer service escalations). Instead, **churn is heavily correlated with digital apathy and lack of baseline engagement.** ## 5 Data-Backed Churn-Risk Hypotheses

Based on visual distribution analysis, we have identified five primary hypotheses to guide our predictive modeling and retention strategies:

**1. The "Silent User" Hypothesis (Web Sessions)**
* *Observation:* Retained users average roughly 6.8 web sessions per 30 days, while churned users average closer to 4.0. 
* *Hypothesis:* A drop in 30-day web sessions is a leading indicator of churn. Retention campaigns should trigger when a user's session frequency drops below 5 per month, rather than waiting for 60 days of total inactivity.

**2. The Abandoned Cart "Sign of Life" Hypothesis**
* *Observation:* Counter-intuitively, retained users have nearly double the rate of abandoned carts (~0.85) compared to churned users (~0.45). 
* *Hypothesis:* Abandoned carts indicate browsing intent and brand consideration. Users who do not abandon carts are not converting perfectly; they simply aren't browsing at all. Marketing should view an abandoned cart as an engagement positive, not just a conversion failure.

**3. The Support Interaction Paradox**
* *Observation:* Retained users log slightly more support tickets on average than churned users. 
* *Hypothesis:* Engaging with support creates a stickier relationship than no engagement at all. Users who experience friction but resolve it are less likely to churn than users who experience friction and silently leave. 

**4. The "Unassigned" Tier Trap**
* *Observation:* The majority of our user base lacks a defined loyalty tier (categorized as "Unassigned"), and this group exhibits a near 1:1 ratio of retained vs. churned users. Conversely, users in the Silver, Gold, and Platinum tiers show significantly better retention ratios.
* *Hypothesis:* The onboarding process is failing to convert users into the loyalty ecosystem. Forcing or incentivizing tier assignment during the first purchase will drastically reduce the 47% baseline churn rate.

**5. The Early Spend Velocity Indicator**
* *Observation:* The boxplot distribution for `total_spend` shows churned customers have a visibly lower median spend and a tighter distribution with fewer high-value outliers compared to retained users.
* *Hypothesis:* Customers who do not break a certain threshold of spend early in their lifecycle are at an extreme risk of churning. We need to define a "minimum viable spend" metric that correlates with long-term retention.

## Next Steps
Before blindly offering discounts to the entire base, we must segment these users. Our next phase will utilize unsupervised machine learning (K-Means Clustering) to group users based on their Recency, Frequency, and Monetary (RFM) metrics to isolate the "silent" at-risk users from the high-value loyalists.
