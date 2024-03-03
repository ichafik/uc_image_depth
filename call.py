import requests
import numpy as np
from PIL import Image
from io import BytesIO
import base64

# Prompt the user to enter depth_min and depth_max values
depth_min = float(input("Enter depth_min value (should be between 9000 and 9560): "))
depth_max = float(input("Enter depth_max value (should be between 9000 and 9560): "))

# Validate the depth_min and depth_max values
if not (9000 <= depth_min <= 9560) or not (9000 <= depth_max <= 9560):
    print("Error: Depth values should be between 9000 and 9560.")
    exit()

# Make a GET request to the Flask server to fetch the images
url = f'http://localhost:50000/images?depth_min={depth_min}&depth_max={depth_max}'
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    try:
        # Parse the JSON response
        data = response.json()

        # Check if the response contains image data
        if 'image' not in data:
            raise ValueError("No image data found in the response.")

        # Decode the base64-encoded image
        image_data = base64.b64decode(data['image'])

        # Create a PIL image from the decoded image data
        image = Image.open(BytesIO(image_data))

        # Save the final concatenated image
        image.save("./data/output/concatenated_image.png")

        print("Image saved successfully.")
    except Exception as e:
        print("Error:", str(e))
else:
    print("Error:", response.text)
