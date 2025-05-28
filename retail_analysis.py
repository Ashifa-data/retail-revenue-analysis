import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create Data
data = {
    'Product': ['T-shirt', 'Jeans', 'Jacket', 'Shoes', 'Cap'],
    'Units_Sold': [150, 90, 60, 110, 200],
    'Price_per_Unit': [40, 120, 200, 150, 20]
}

df = pd.DataFrame(data)

# Step 2: Calculate Total Revenue
df['Total_Revenue'] = df['Units_Sold'] * df['Price_per_Unit']

# Step 3: Show Top Product
top_product = df.loc[df['Total_Revenue'].idxmax(), 'Product']
print(f"Top revenue-generating product: {top_product}")

# Step 4: Visualize
plt.figure(figsize=(8, 5))
plt.bar(df['Product'], df['Total_Revenue'], color='teal')
plt.title('Total Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue (QAR)')
plt.tight_layout()
plt.savefig("revenue_chart.png")
plt.show()
