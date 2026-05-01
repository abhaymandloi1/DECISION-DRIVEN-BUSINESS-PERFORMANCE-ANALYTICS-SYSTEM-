SELECT 
    p.product_category_name,
    SUM(oi.price) AS revenue,
    COUNT(*) AS items_sold
FROM dbo.olist_order_items_dataset oi
JOIN dbo.olist_products_dataset p
    ON oi.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY revenue DESC;