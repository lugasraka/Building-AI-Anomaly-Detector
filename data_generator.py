import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_building_data(days=30):
    # Create a time range
    date_range = pd.date_range(start=datetime.now() - timedelta(days=days), end=datetime.now(), freq='h')
    n = len(date_range)

    # 1. Base Load (Simulate daily cycles)
    # Buildings use more power during the day (8am-6pm)
    hour_of_day = date_range.hour
    base_load = 50 + 50 * np.sin((hour_of_day - 6) * np.pi / 12)**2
    base_load = base_load.to_numpy()  # Convert to numpy array for mutable operations
    
    # 2. Add Weekend Drop (Buildings use less power on weekends)
    day_of_week = date_range.dayofweek.to_numpy()  # Convert to numpy array
    is_weekend = day_of_week >= 5
    base_load[is_weekend] *= 0.4  # 60% reduction on weekends

    # 3. Add Random Noise (Sensor fluctuations)
    noise = np.random.normal(0, 5, n)
    
    # 4. Inject Anomalies (The "Faults" we want to detect)
    # Randomly spike energy usage at 10 random points
    anomalies = np.zeros(n)
    indices = np.random.choice(np.arange(n), size=15, replace=False)
    anomalies[indices] = np.random.uniform(50, 100, size=15) # Big spikes

    total_load = base_load + noise + anomalies

    # Create DataFrame
    df = pd.DataFrame({
        'timestamp': date_range,
        'energy_kwh': total_load,
        'outdoor_temp': 25 + 5 * np.sin((hour_of_day - 10) * np.pi / 12) + np.random.normal(0, 2, n)
    })
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Save
    df.to_csv('data/building_data.csv', index=False)
    print("Data generated in data/building_data.csv")

if __name__ == "__main__":
    generate_building_data()