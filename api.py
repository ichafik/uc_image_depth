import pandas as pd
import base64
from io import BytesIO
import numpy as np
from PIL import Image

from flask import Flask, request, render_template
from sqlalchemy import create_engine, Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from utils import process_and_save_image

app = Flask(__name__, template_folder='./templates')

# Define SQLAlchemy engine and base
engine = create_engine('sqlite:///data.db', echo=True)
Base = declarative_base()

# Define ORM class for image data
class ImageData(Base):
    __tablename__ = 'image_data'
    id = Column(Integer, primary_key=True)
    image_data = Column(String)
    depth = Column(Float)  

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

@app.route("/images", methods=["GET"])
def get_images():
    """
    Retrieve images from the database based on depth range parameters
    and construct HTML to display the concatenated image.

    Returns:
        str: HTML code containing the concatenated image.
    """
    # Retrieve depth range parameters from request
    depth_min = float(request.args.get("depth_min"))
    depth_max = float(request.args.get("depth_max"))

    # Retrieve base64-encoded image data from the database based on depth range
    images_data = session.query(ImageData).filter(ImageData.depth >= depth_min, ImageData.depth <= depth_max).all()

    # Initialize variables to store image dimensions
    image_arrays = []

    for image_data in images_data:
        image_bytes = base64.b64decode(image_data.image_data)
        pil_image = Image.open(BytesIO(image_bytes))
        image_array = np.array(pil_image)
        image_arrays.append(image_array)
    final_image = np.concatenate(image_arrays, axis=0)

    # Convert concatenated image to base64
    with BytesIO() as buffer:
        final_image_pil = Image.fromarray(final_image)
        final_image_pil.save(buffer, format="PNG")
        buffer.seek(0)
        base64_image = base64.b64encode(buffer.getvalue()).decode("utf-8")

    # Construct HTML image tag
    image_html = f'<img src="data:image/png;base64,{base64_image}" alt="Concatenated Image">'

    return render_template("index.html", image_html=image_html)

if __name__ == "__main__":
    # Load data
    df = pd.read_csv("./data/data.csv")
    # Process and save image to database
    process_and_save_image(session, df)
    # Run the Flask app
    app.run(host='0.0.0.0', port=50000, debug=True)
