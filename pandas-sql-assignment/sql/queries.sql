-- Q1: Basic SELECT
SELECT order_id, customer_id, quantity, revenue
FROM orders
LIMIT 5;

-- Q2: WHERE clause
SELECT order_id, customer_id, revenue
FROM orders
WHERE revenue > 5000
ORDER BY revenue DESC
LIMIT 5;

-- Q3: ORDER BY
SELECT order_id, discount, revenue
FROM orders
ORDER BY discount DESC
LIMIT 5;

-- Q4: Aggregate functions
SELECT
    COUNT(*)               AS total_orders,
    ROUND(SUM(revenue),2)  AS total_revenue,
    ROUND(AVG(revenue),2)  AS avg_revenue,
    ROUND(MIN(revenue),2)  AS min_revenue,
    ROUND(MAX(revenue),2)  AS max_revenue
FROM orders;

-- Q5: GROUP BY
SELECT ship_mode,
       COUNT(*)               AS total_orders,
       ROUND(SUM(revenue),2)  AS total_revenue
FROM orders
GROUP BY ship_mode
ORDER BY total_revenue DESC;

-- Q6: INNER JOIN
SELECT o.order_id,
       c.customer_name,
       c.region,
       c.segment,
       ROUND(o.revenue,2) AS revenue
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
LIMIT 5;

-- Q7: JOIN + GROUP BY
SELECT p.category,
       COUNT(*)                AS total_orders,
       ROUND(SUM(o.revenue),2) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;

-- Q8: Three-table JOIN
SELECT o.order_id,
       c.region,
       c.segment,
       p.category,
       o.quantity,
       ROUND(o.revenue,2) AS revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products  p ON o.product_id  = p.product_id
LIMIT 5;

-- Q9: HAVING
SELECT c.customer_name,
       COUNT(o.order_id)        AS total_orders,
       ROUND(SUM(o.revenue),2)  AS total_spent
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING total_spent > 10000
ORDER BY total_spent DESC
LIMIT 5;

-- Q10: Subquery
SELECT order_id, ROUND(revenue,2) AS revenue
FROM orders
WHERE revenue > (SELECT AVG(revenue) FROM orders)
ORDER BY revenue DESC
LIMIT 5;

-- Q11: Revenue by Region
SELECT c.region,
       COUNT(*)                  AS total_orders,
       ROUND(SUM(o.revenue),2)   AS total_revenue,
       ROUND(AVG(o.revenue),2)   AS avg_revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.region
ORDER BY total_revenue DESC;

-- Q12: Top 5 Products
SELECT p.product_id,
       p.category,
       ROUND(SUM(o.revenue),2)  AS total_revenue,
       SUM(o.quantity)          AS units_sold
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_id, p.category
ORDER BY total_revenue DESC
LIMIT 5;

-- Q13: Monthly Revenue Trend
SELECT month,
       ROUND(SUM(revenue),2)  AS monthly_revenue,
       COUNT(*)               AS order_count
FROM orders
GROUP BY month
ORDER BY month;

-- Q14: Multi-column GROUP BY
SELECT c.segment,
       p.category,
       ROUND(SUM(o.revenue),2) AS total_revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products  p ON o.product_id  = p.product_id
GROUP BY c.segment, p.category
ORDER BY c.segment, total_revenue DESC;

-- Q15: Nested Subquery
SELECT region, total_revenue
FROM (
    SELECT c.region,
           ROUND(SUM(o.revenue),2) AS total_revenue
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    GROUP BY c.region
) AS region_totals
WHERE total_revenue = (
    SELECT MAX(sub.total_revenue)
    FROM (
        SELECT c.region, SUM(o.revenue) AS total_revenue
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        GROUP BY c.region
    ) AS sub
);