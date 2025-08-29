# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies for both FastAPI and Flask
COPY backend-fastapi/requirements.txt /app/fastapi-requirements.txt
RUN pip install --no-cache-dir -r fastapi-requirements.txt

COPY backend-flask/requirements.txt /app/flask-requirements.txt
RUN pip install --no-cache-dir -r flask-requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose ports for FastAPI and Flask
EXPOSE 8000 8080

# Command to run the FastAPI application
CMD ["uvicorn", "backend-fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
