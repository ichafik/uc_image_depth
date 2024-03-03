# import sqlite3

# # Connect to the SQLite database
# conn = sqlite3.connect('data.db')
# cursor = conn.cursor()

# # Execute a query to fetch all records from the 'data' table
# cursor.execute("SELECT * FROM data")

# # Fetch all rows from the result set
# rows = cursor.fetchall()

# # Print the rows
# for row in rows:
#     print(row)

# # Close the connection
# conn.close()


import os
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Define SQLAlchemy engine
engine = create_engine('sqlite:///data.db', echo=True)

# Define SQLAlchemy base
Base = declarative_base()


# Close existing session if it exists
if 'session' in locals():
    session.close()

from sqlalchemy.sql import text

# Drop the image_data table
with engine.connect() as connection:
    connection.execute(text("DROP TABLE IF EXISTS image_data"))

# Recreate all tables
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()
