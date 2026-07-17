import sqlite3
import pandas as pd

# Load CSV
df = pd.read_csv("data/retail_store_inventory.csv")

# Create SQLite database
conn = sqlite3.connect("database/retail.db")

# Store data in SQLite
df.to_sql("retail_data", conn, if_exists="replace", index=False)

print("✅ Database created successfully!")

# Show number of records
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM retail_data")

print("Rows inserted:", cursor.fetchone()[0])

conn.close()

#TO CREATE DATABASE FROM CSV