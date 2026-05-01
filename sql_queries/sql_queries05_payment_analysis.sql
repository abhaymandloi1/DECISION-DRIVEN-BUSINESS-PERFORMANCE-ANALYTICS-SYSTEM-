SELECT 
    payment_type,
    COUNT(*) AS payment_count,
    SUM(payment_value) AS total_payment
FROM dbo.olist_order_payments_dataset
GROUP BY payment_type
ORDER BY total_payment DESC;