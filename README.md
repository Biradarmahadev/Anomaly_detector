# Real-Time IoT Anomaly Detection System

This project implements a real-time anomaly detection system for IoT devices using time-series analysis and machine learning techniques.

## Features

- Real-time data ingestion using InfluxDB
- Time-series anomaly detection using Autoencoder and Isolation Forest
- Visualizations of sensor data and anomalies
- Configurable alert thresholds
- Support for multiple sensor types (temperature, humidity, etc.)

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure InfluxDB connection in `.env` file

3. Run the data ingestion script:
```bash
python data_ingestion.py
```

4. Train and run the anomaly detection model:
```bash
python anomaly_detector.py
```

## Project Structure

- `data/`: Contains sample datasets and processed data
- `models/`: Contains ML model implementations
- `utils/`: Utility functions and configurations
- `notebooks/`: Jupyter notebooks for experimentation

## Requirements

- Python 3.8+
- InfluxDB 2.x
- TensorFlow 2.8+
- Other dependencies listed in requirements.txt
