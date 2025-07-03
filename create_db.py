import sqlite3

# Connect to database (it will create the file if it doesn't exist)
conn = sqlite3.connect('sales_data.db')

# Create sales table
conn.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
''')

# Insert sample data
sample_data = [
    ('Apple', 10, 2.5),
    ('Banana', 20, 1.0),
    ('Orange', 15, 1.8),
    ('Apple', 5, 2.5),
    ('Banana', 10, 1.0)
]
conn.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sample_data)

# Save and close
conn.commit()
conn.close()

print("Database created and data inserted!")
