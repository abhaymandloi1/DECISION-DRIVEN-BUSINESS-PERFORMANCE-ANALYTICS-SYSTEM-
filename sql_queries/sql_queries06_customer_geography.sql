SELECT TOP 10
    customer_city,
    COUNT(*) AS total_customers
FROM dbo.olist_customers_dataset
GROUP BY customer_city
ORDER BY total_customers DESC;