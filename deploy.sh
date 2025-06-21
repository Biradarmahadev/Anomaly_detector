#!/bin/bash

# Exit on error
set -e

# Build the Docker image
echo "Building Docker image..."
docker-compose build

# Start the services
echo "Starting services..."
docker-compose up -d

echo "\nDeployment complete!"
echo "Anomaly Detector is running on http://localhost:5000"
echo "InfluxDB UI is available at http://localhost:8086"

echo "\nTo view logs, run: docker-compose logs -f"
echo "To stop the services, run: docker-compose down"
