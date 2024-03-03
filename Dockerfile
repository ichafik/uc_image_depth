# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all necessary files into the container
COPY api.py .
COPY utils.py .
COPY data ./data
COPY templates ./templates
COPY query ./query

# Command to run the Flask server
CMD ["python", "api.py"]
