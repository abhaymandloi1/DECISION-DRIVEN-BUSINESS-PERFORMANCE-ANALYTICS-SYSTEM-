import pyodbc
import pandas as pd

# Connection details
server = 'DESKTOP-IM6F1C4\\SQLEXPRESS'
database = 'olist_analytics'

# Connect to SQL Server
conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'
)

print("Connection successful!")

# Query data
query = "SELECT * FROM dbo.dashboard_dataset"

df = pd.read_sql(query, conn)
print("\nColumns in dataset:")
print(df.columns)

print(df.head())

print("\nBasic Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
plt.ion()

# Convert date column to datetime
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# Create month column
df['order_month'] = df['order_purchase_timestamp'].dt.to_period('M')

# Group data
monthly_sales = df.groupby('order_month')['price'].sum().reset_index()

# Sort data
monthly_sales = monthly_sales.sort_values('order_month')

# Remove last incomplete month
monthly_sales = monthly_sales.iloc[:-1]

# Convert to string for plotting
monthly_sales['order_month'] = monthly_sales['order_month'].astype(str)

# Plot


plt.figure(figsize=(10,5))
plt.plot(monthly_sales['order_month'], monthly_sales['price'])
plt.xticks(rotation=45)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

# Top 10 cities by number of customers
top_cities = df['customer_city'].value_counts().head(10)

print("\nTop 10 Cities:")
print(top_cities)
plt.figure(figsize=(10,5))
top_cities.plot(kind='bar')
plt.title("Top 10 Customer Cities")
plt.xlabel("City")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_cities.png")
plt.show()


# Payment type distribution
payment_data = df.groupby('payment_type').agg({
    'payment_value': 'sum',
    'order_id': 'count'
}).reset_index()

print("\nPayment Analysis:")
print(payment_data)
plt.figure(figsize=(8,5))
plt.bar(payment_data['payment_type'], payment_data['payment_value'])
plt.title("Revenue by Payment Type")
plt.xlabel("Payment Type")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("payment_analysis.png")
plt.show()

"""# Convert delivery dates to datetime
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# Calculate delivery time (in days)

df['delivery_days'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days

print("\nDelivery Time Sample:")
print(df[['order_id', 'delivery_days']].head())
# Remove negative or missing delivery times
delivery_df = df[df['delivery_days'] > 0]
avg_delivery = delivery_df['delivery_days'].mean()

print("\nAverage Delivery Time:", avg_delivery)

plt.figure(figsize=(8,5))
plt.hist(delivery_df['delivery_days'], bins=30)
plt.title("Delivery Time Distribution")
plt.xlabel("Days")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("delivery_distribution.png")
plt.show()"""


# ========================
# PRODUCT CATEGORY ANALYSIS
# ========================

top_products = df.groupby('product_category_name')['price'].sum().sort_values(ascending=False).head(10)

print("\nTop Product Categories:")
print(top_products)
plt.figure(figsize=(10,5))
top_products.plot(kind='bar')
plt.title("Top Product Categories by Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_products.png")
plt.show()