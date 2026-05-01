SELECT 
    order_id,
    order_purchase_timestamp,
    YEAR(order_purchase_timestamp) AS order_year,
    MONTH(order_purchase_timestamp) AS order_month,
    order_status,
    customer_city,
    customer_state,
    product_category_name,
    price,
    freight_value,
    payment_type,
    payment_value
FROM dbo.master_business_dataset;