
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect('sales_data.db')

# Run SQL query
query = """
    SELECT product, 
           SUM(quantity) AS total_qty, 
           SUM(quantity * price) AS revenue
    FROM sales
    GROUP BY product
"""
df = pd.read_sql_query(query, conn)

# Print results
print("\nSales Summary:")
print(df)

# Plot bar chart
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title('Revenue per Product')
plt.ylabel('Revenue')
plt.xlabel('Product')
plt.tight_layout()
plt.savefig('sales_chart.png')
plt.show()

# Close the connection
conn.close()
