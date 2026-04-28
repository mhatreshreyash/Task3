# Import pandas library
import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("sales_data.csv")

# Step 2: Display first few rows
print("Dataset Preview:")
print(df.head())

# Step 3: Handle missing values
df['Product'] = df['Product'].fillna('Unknown')
df['Quantity'] = df['Quantity'].fillna(0)
df['Price'] = df['Price'].fillna(0)

# Step 4: Create Total Sales column
df['Total_Sales'] = df['Quantity'] * df['Price']

# Step 5: Calculate metrics

# Total Sales
total_sales = df['Total_Sales'].sum()

# Best-selling product (by quantity)
best_product = df.groupby('Product')['Quantity'].sum().idxmax()

# Top revenue product
top_revenue_product = df.groupby('Product')['Total_Sales'].sum().idxmax()

# Average sales per transaction
avg_sales = df['Total_Sales'].mean()

# Step 6: Print report
print("\n" + "="*40)
print("SALES ANALYSIS REPORT")
print("="*40)

print(f"Total Sales: ₹{total_sales:.2f}")
print(f"Best-Selling Product: {best_product}")
print(f"Top Revenue Product: {top_revenue_product}")
print(f"Average Sales per Transaction: ₹{avg_sales:.2f}")

print("="*40)

# Step 7: Save report to file (FIXED UTF-8 ERROR)
with open("sales_report.txt", "w", encoding="utf-8") as f:
    f.write("SALES ANALYSIS REPORT\n")
    f.write("="*40 + "\n")
    f.write(f"Total Sales: ₹{total_sales:.2f}\n")
    f.write(f"Best-Selling Product: {best_product}\n")
    f.write(f"Top Revenue Product: {top_revenue_product}\n")
    f.write(f"Average Sales per Transaction: ₹{avg_sales:.2f}\n")
    f.write("="*40)

print("\n✅ Report saved successfully as 'sales_report.txt'")
