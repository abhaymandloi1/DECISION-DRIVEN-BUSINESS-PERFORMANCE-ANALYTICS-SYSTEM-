ALTER VIEW dbo.dashboard_dataset AS
SELECT
    m.order_id,
    m.order_purchase_timestamp,
    YEAR(m.order_purchase_timestamp) AS order_year,
    MONTH(m.order_purchase_timestamp) AS order_month,
    DATENAME(MONTH, m.order_purchase_timestamp) AS month_name,
    m.order_status,
    m.customer_city,
    m.customer_state,

    -- FIX HERE
    ISNULL(t.column2, m.product_category_name) AS product_category_name,

    m.price,
    m.freight_value,
    m.payment_type,
    m.payment_value

FROM dbo.master_business_dataset m

LEFT JOIN dbo.product_category_name_translation t
ON m.product_category_name = t.column1;