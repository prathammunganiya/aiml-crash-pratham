# Order Delay Intelligence — Project Report
**Internship:** CodeTrade.io | DecodeLabs Batch 2026  
**Dataset:** Brazilian E-Commerce Public Dataset (Olist)

---

## 1. Project Overview
The goal of this project is to predict whether an e-commerce 
order will be delayed, and explain the key factors driving 
those delays using machine learning.

---

## 2. Dataset Summary
| File | Key Columns |
|------|-------------|
| olist_orders_dataset.csv | order_id, dates, status |
| olist_order_payments_dataset.csv | payment_type, value |
| olist_customers_dataset.csv | customer_state |
| olist_order_items_dataset.csv | freight_value, price |
| olist_products_dataset.csv | product_category |

---

## 3. EDA Findings
1. **6.8%** of delivered orders were delayed 
   beyond the estimated delivery date.
2. Delay rates peak in **month 3** — likely due 
   to seasonal demand changes.
3. Orders placed on weekends show higher delay rates 
   than weekday orders.
4. Delivery time in days strongly correlates with delay — 
   longer shipments delay more.
5. State **AL** has the highest delay rate 
   among all customer states.

---

## 4. SQL Insights
- Top 5 states by order volume: SP, RJ, MG, RS, PR
- Most common payment method: credit_card
- One pandas insight recreated in SQL and outputs matched

---

## 5. Model Comparison

### Metrics on Test Set
| Metric | Logistic Regression | XGBoost (Tuned) |
|--------|-------------------|-----------------|
| Accuracy  | 0.9601  | 0.9656  |
| Precision | 0.7909 | 0.7949 |
| Recall    | 0.5585  | 0.6641  |
| F1-Score  | 0.6547   | 0.7236   |
| ROC-AUC   | 0.9540  | 0.9804  |

### Cross-Validation Results (5-Fold Stratified)
| Model | Mean F1 | Std Dev |
|-------|---------|---------|
| Logistic Regression | 0.6571  | ±0.0057  |
| XGBoost (Tuned)     | 0.7250 | ±0.0048 |

### Best Hyperparameters (GridSearchCV)
- `max_depth`: 7
- `learning_rate`: 0.1

---

## 6. Most Important Metric: Recall
For this business problem, **Recall** matters most.
A False Negative means the company takes no action —
leading to unhappy customers and bad reviews.
High Recall ensures we catch most real delays early
so the business can act proactively.

---

## 7. SHAP Feature Importance
Top features driving delay predictions:
1. `delivery_time_days` — highest impact
2. `freight_value` — higher freight = more delay risk
3. `purchase_month` — seasonal effect
4. `item_count` — more items = more delay risk
5. `payment_value` — order size matters

---

## 8. Business Recommendations
1. Flag orders with delivery_time_days > 15 for alerts.
2. Increase logistics capacity in month 3.
3. Investigate high-delay state AL with carriers.
4. High freight value orders need priority tracking.

---

## 9. Conclusion
XGBoost outperformed Logistic Regression across all metrics.
SHAP confirmed delivery time and freight value are the 
strongest predictors of delay. With proper monitoring, 
the business can reduce delays by acting on these signals.
