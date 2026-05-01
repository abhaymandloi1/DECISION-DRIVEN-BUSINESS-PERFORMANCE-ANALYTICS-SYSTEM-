CREATE VIEW master_business_dataset AS
SELECT 
    o.order_id,
    o.order_purchase_timestamp,
    o.order_status,
    c.customer_city,
    c.customer_state,
    p.product_category_name,
    oi.price,
    oi.freight_value,
    pay.payment_type,
    pay.payment_value
FROM dbo.olist_orders_dataset o
JOIN dbo.olist_customers_dataset c
    ON o.customer_id = c.customer_id
JOIN dbo.olist_order_items_dataset oi
    ON o.order_id = oi.order_id
JOIN dbo.olist_products_dataset p
    ON oi.product_id = p.product_id
JOIN dbo.olist_order_payments_dataset pay
    ON o.order_id = pay.order_id;