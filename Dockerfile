# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variables from .env file
# Note: In production, these should be set in the deployment environment
# ENV INFLUXDB_URL=your_influxdb_url
# ENV INFLUXDB_TOKEN=your_influxdb_token
# ENV INFLUXDB_ORG=your_influxdb_org
# ENV INFLUXDB_BUCKET=your_influxdb_bucket

# Run anomaly_detector.py when the container launches
CMD ["python", "anomaly_detector.py"]
