import pandas as pd
from pyod.models.copod import COPOD

class AnomalyDetector:
    def __init__(self, contamination=0.05):
        # Contamination is the % of data we expect to be anomalies (5%)
        self.model = COPOD(contamination=contamination)

    def train_and_predict(self, df):
        # We use 'energy_kwh' and 'outdoor_temp' features
        X = df[['energy_kwh', 'outdoor_temp']]
        
        # Train model
        self.model.fit(X)
        
        # Predict: 1 is anomaly, 0 is normal (PyOD convention)
        df['anomaly_score'] = self.model.decision_scores_
        df['is_anomaly'] = self.model.labels_
        
        # Convert to boolean (True) for easier filtering
        df['is_anomaly'] = df['is_anomaly'] == 1
        return df
