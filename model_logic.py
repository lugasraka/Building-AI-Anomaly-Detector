import pandas as pd
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self, contamination=0.05):
        # Contamination is the % of data we expect to be anomalies (5%)
        self.model = IsolationForest(contamination=contamination)

    def train_and_predict(self, df):
        # We use 'energy_kwh' and 'outdoor_temp' features
        X = df[['energy_kwh', 'outdoor_temp']]
        
        # Train model
        self.model.fit(X)
        
        # Predict: -1 is anomaly, 1 is normal
        df['anomaly_score'] = self.model.decision_function(X)
        df['is_anomaly'] = self.model.predict(X)
        
        # Convert -1 to boolean (True) for easier filtering
        df['is_anomaly'] = df['is_anomaly'] == -1
        return df