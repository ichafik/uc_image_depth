import base64
from io import BytesIO
import numpy as np
from PIL import Image
from flask import Flask, request, render_template
from sqlalchemy import create_engine, Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define SQLAlchemy engine and base
engine = create_engine('sqlite:///data.db', echo=True)
Base = declarative_base()

# Define ORM class for image data

class ImageData(Base):
    __tablename__ = 'image_data'
    id = Column(Integer, primary_key=True)
    image_data = Column(String)
    depth = Column(Float)  # Add depth column




def process_and_save_image(session, df):
    """
    Process the DataFrame to generate images, resize them to a width of 150 pixels,
    and save the base64-encoded image data along with the depth information into the database.

    Parameters:
        session (sqlalchemy.orm.session.Session): SQLAlchemy session object for database interaction.
        df (pandas.DataFrame): DataFrame containing the image data.

    Returns:
        None
    """
    # Initialize variables
    desired_width = 150
    aspect_ratio = desired_width / 200  # New width / Original width

    # Resize the height accordingly
    desired_height = int(10 * aspect_ratio)
    image_shape = (desired_height, desired_width)

    for idx, row in df.iterrows():
        # Extract depth and image data
        depth = row['depth']
        pixel_values = row.values[1:].astype(np.uint8)

        # Reshape the image
        image_array = pixel_values.reshape(10, 20)

        # Resize the image
        resized_image = Image.fromarray(image_array).resize((desired_width, desired_height))

        # Convert the resized image to base64
        with BytesIO() as buffer:
            resized_image.save(buffer, format="PNG")
            buffer.seek(0)
            image_bytes = buffer.getvalue()
            base64_image = base64.b64encode(image_bytes).decode("utf-8")

        # Save base64 encoded image and depth to the database
        image_data = ImageData(image_data=base64_image, depth=depth)
        session.add(image_data)

    session.commit()
