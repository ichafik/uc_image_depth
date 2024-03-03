import pandas as pd
from PIL import Image
from io import BytesIO
import base64
from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)

app = Flask(__name__, template_folder='./templates')

# Load data
df = pd.read_csv("./data/data.csv")

###
## TBD: Reshape dataframe
## TBD: Store data in Sqlite3

@app.route("/images", methods=["GET"])
def get_images():
    ## TBD: Read data from Sqlite3
    depth_min = float(request.args.get("depth_min"))
    depth_max = float(request.args.get("depth_max"))
    filtered_df = df[(df["depth"] >= depth_min) & (df["depth"] <= depth_max)]

    # Initialize variables to store image dimensions
    num_rows = len(filtered_df)
    image_shape = (10, 20)

    image_arrays = []
    # Loop through each row in the filtered DataFrame, optimization potential to avoid loop 
    for idx, row in filtered_df.iterrows():
        pixel_values = row.iloc[1:].values.astype(np.uint8)

        if pixel_values.size != np.prod(image_shape):
            raise ValueError("Pixel values size does not match the image shape.")

        image_array = pixel_values.reshape(image_shape)
        image_arrays.append(image_array)

    final_image = np.concatenate(image_arrays, axis=0)
    final_image_pil = Image.fromarray(final_image)

    with BytesIO() as buffer:
        final_image_pil.save(buffer, format="PNG")
        buffer.seek(0)
        image_bytes = buffer.getvalue()
        base64_image = base64.b64encode(image_bytes).decode("utf-8")

    image_html = f'<img src="data:image/png;base64,{base64_image}" alt="Concatenated Image">'

    return render_template("index.html", image_html=image_html)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=50000, debug=True)
