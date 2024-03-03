# Docker Flask Image with Image Reshaping and SQLite Integration

This repository contains a Dockerized Flask application named "image_depth" with functionality for image reshaping and integration with SQLite3. The application serves images based on specified depth ranges.

## Components

### Dockerfile
The Dockerfile uses the official Python 3.9-slim base image and sets up the necessary environment for running the Flask application. Here are the key steps:

1. **Setting Working Directory**: Sets the working directory in the container to `/app`.
2. **Copying Files**: Copies the `requirements.txt` file, `api.py`, `call.py`, and the `data` and `templates` directories into the container.
3. **Installing Dependencies**: Installs the required Python packages listed in `requirements.txt` using `pip`.
4. **Command to Run**: Specifies the command to run the Flask server by executing `python api.py`.

### requirements.txt
Contains the Python dependencies required for the Flask application:

- pandas
- flask
- pillow
- numpy
- matplotlib

### api.py
This Python script implements the Flask application with the following functionality:

- **Loading Data**: Reads the image data from a CSV file located in the `data` directory into a pandas DataFrame (`df`).
- **Image Reshaping (TBD)**: This part of the code is to be determined. It will handle reshaping the DataFrame to fit the desired image dimensions.
- **Storing Data in SQLite3 (TBD)**: This part of the code is to be determined. It will handle storing the reshaped data in a SQLite3 database.
- **Serving Images**: Defines an endpoint `/images` that accepts GET requests with parameters `depth_min` and `depth_max`. It filters the DataFrame based on the specified depth range and serves the corresponding images.
- **Image Processing**: Processes the filtered DataFrame to generate the final image to be served.
- **Rendering HTML**: Embeds the processed image in HTML and renders it using the `index.html` template.

## Usage
To build and run the Docker image, navigate to the directory containing the Dockerfile and run the following commands:

```bash
docker build -t image_depth .
docker run -p 50000:50000 image_depth
```

Once the container is running, you can access the Flask application at `http://localhost:50000/images` in your web browser.

## TBD (To Be Determined)
- **Reshape DataFrame**: Implement the logic to reshape the DataFrame (`df`) to fit the desired image dimensions.
- **Store Data in SQLite3**: Implement the logic to store the reshaped data in a SQLite3 database.

These points need further development to complete the functionality of the application.