# Example: Dockerfile for the AI module

FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install required dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the code
COPY . .

# Run the AI prediction script
CMD ["python", "predict.py"]
