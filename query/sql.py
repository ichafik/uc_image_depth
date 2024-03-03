import os
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text


# Define SQLAlchemy engine
engine = create_engine('sqlite:///data.db', echo=True)

# Define SQLAlchemy base
Base = declarative_base()


# Close existing session if it exists
if 'session' in locals():
    session.close()

# Drop the image_data table
with engine.connect() as connection:
    connection.execute(text("DROP TABLE IF EXISTS image_data"))

# Recreate all tables
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()
