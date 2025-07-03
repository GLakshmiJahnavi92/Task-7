# Task 7: Basic Sales Summary from SQLite Database

## ✅ What I did
- Created a small SQLite database (`sales_data.db`) with sample sales data.
- Wrote Python scripts to insert data and summarize it.
- Ran SQL queries inside Python using `sqlite3`.
- Loaded the query results into a pandas DataFrame.
- Printed the summary and created a bar chart using matplotlib.

## 📂 Files
| File | Description |
|-----|-------------|
| `create_db.py` | Script to create the database and insert sample data |
| `sales_summary.py` | Script to run SQL query, print summary, and plot chart |
| `sales_data.db` | SQLite database file |
| `sales_chart.png` | Generated chart of revenue by product |

## 🛠 How to run
1. Run `create_db.py` to create the database and insert data:
```bash
python create_db.py
```

2. Run `sales_summary.py` to see the summary and generate the chart:
```bash
python sales_summary.py
```

The chart will also be saved as `sales_chart.png`.

## 📊 What the SQL query does
```sql
SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
```
- Groups sales by product
- Calculates total quantity and total revenue for each product

## ⭐ What I learned
- Using SQLite with Python (`sqlite3`)
- Running SQL queries inside Python
- Loading data into pandas DataFrame
- Visualizing results with matplotlib
