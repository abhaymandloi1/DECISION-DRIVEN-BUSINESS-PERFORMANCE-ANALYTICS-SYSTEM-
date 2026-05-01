SELECT TOP 10
    seller_state,
    COUNT(*) AS total_sellers
FROM dbo.olist_sellers_dataset
GROUP BY seller_state
ORDER BY total_sellers DESC;