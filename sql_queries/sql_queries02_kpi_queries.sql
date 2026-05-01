SELECT 
    SUM(price) AS total_revenue
FROM dbo.olist_order_items_dataset;
SELECT 
    COUNT(DISTINCT order_id) AS total_orders
FROM dbo.olist_orders_dataset;
SELECT 
    COUNT(DISTINCT customer_id) AS total_customers
FROM dbo.olist_customers_dataset;
SELECT 
    SUM(price) / COUNT(DISTINCT order_id) AS avg_order_value
FROM dbo.olist_order_items_dataset;
SELECT 
    order_status,
    COUNT(*) AS order_count
FROM dbo.olist_orders_dataset
GROUP BY order_status
ORDER BY order_count DESC;