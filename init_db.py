# init_db.py
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('app.db')
cursor = conn.cursor()

# Commit changes and close connection
conn.commit()
conn.close()