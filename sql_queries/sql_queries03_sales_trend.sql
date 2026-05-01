SELECT 
    FORMAT(o.order_purchase_timestamp,'yyyy-MM') AS order_month,
    SUM(oi.price) AS monthly_revenue,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM dbo.olist_orders_dataset o
JOIN dbo.olist_order_items_dataset oi
    ON o.order_id = oi.order_id
GROUP BY FORMAT(o.order_purchase_timestamp,'yyyy-MM')
ORDER BY order_month;