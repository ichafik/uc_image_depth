# import pandas as pd
# from PIL import Image
# import numpy as np

# def load_data(filepath):
#     df = pd.read_csv(filepath)
#     return df

# def preprocess_image(image_data, new_width=150):
#     image_array = np.array(image_data).reshape((-1, 200))
#     resized_image = Image.fromarray(image_array).resize((new_width, int(200 * new_width / 200)))
#     return resized_image
