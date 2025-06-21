import os
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import json
from dotenv import load_dotenv
from sklearn.preprocessing import StandardScaler

# Load environment variables
load_dotenv()

class IoTAnomalyDetector:
    def __init__(self):
        self.autoencoder = None
        self.isolation_forest = None
        self.threshold = None
        
    def train_isolation_forest(self, X_train):
        """Train the Isolation Forest model"""
        self.isolation_forest = IsolationForest(contamination=0.01)
        self.isolation_forest.fit(X_train)
    
    def detect_anomalies(self, data):
        """Detect anomalies using Isolation Forest"""
        # Standardize the data
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data)
        
        # Get anomaly predictions
        predictions = self.isolation_forest.predict(data_scaled)
        
        # Convert predictions to binary (1 for anomaly, 0 for normal)
        anomalies = np.where(predictions == -1, 1, 0)
        
        # Get anomaly scores
        scores = self.isolation_forest.decision_function(data_scaled)
        
        return anomalies, scores
    
    def visualize_results(self, data, anomalies, scores):
        """Visualize the results"""
        plt.figure(figsize=(15, 6))
        plt.plot(data, label='Sensor Data')
        plt.plot(anomalies * np.max(data), 'ro', markersize=5, label='Anomalies')
        plt.title('Anomaly Detection Results')
        plt.xlabel('Time')
        plt.ylabel('Sensor Value')
        plt.legend()
        plt.show()
        
        plt.figure(figsize=(15, 6))
        plt.plot(scores, label='Anomaly Score')
        plt.title('Anomaly Scores')
        plt.xlabel('Time')
        plt.ylabel('Score')
        plt.legend()
        plt.show()

def main():
    # Example usage
    # Create a sample dataset (in practice, this would come from InfluxDB)
    np.random.seed(42)
    data = np.sin(np.linspace(0, 10, 1000)) + np.random.normal(0, 0.1, 1000)
    data = data.reshape(-1, 1)
    
    # Add some anomalies
    data[200:210] += 2
    data[400:410] -= 2
    
    # Initialize and train the detector
    detector = IoTAnomalyDetector()
    detector.train_isolation_forest(data[:800])
    
    # Detect anomalies
    anomalies, scores = detector.detect_anomalies(data)
    
    # Visualize results
    detector.visualize_results(data, anomalies, scores)

if __name__ == "__main__":
    main()
