Dockerfile for a "Hello, World!" Python program:

Dockerfile
# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Run the Python script when the container launches
CMD ["python", "hello_world.py"]


Make sure you have a Python script named hello_world.py in the same directory as the Dockerfile, containing your "Hello, World!" program.

Build the Docker image using the following command:

bash
docker build -t your-image-name .


Replace "your-image-name" with the desired name for your Docker image. After building, you can run the Docker container:

bash
docker run your-image-name


This will execute your Python script within the Docker container, displaying the "Hello, World!" output.