import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect('sales_data.db')

# SQL query to get total quantity & revenue per product
query = '''
SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
'''

# Load results into pandas DataFrame
df = pd.read_sql_query(query, conn)

# Print the summary
print(df)

# Plot revenue by product
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title('Revenue by Product')
plt.ylabel('Revenue')
plt.xlabel('Product')
plt.tight_layout()
plt.savefig('sales_chart.png')  # Save chart as image
plt.show()

conn.close()

