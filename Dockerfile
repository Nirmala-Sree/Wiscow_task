# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any necessary dependencies (based on requirements.txt)
RUN pip install -r requirements.txt

# Expose port 5000 for Flask to run
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]
