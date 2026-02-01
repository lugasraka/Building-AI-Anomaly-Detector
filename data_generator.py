import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_building_data(days=30):
    # Create a time range
    date_range = pd.date_range(start=datetime.now() - timedelta(days=days), end=datetime.now(), freq='h')
    n = len(date_range)
    hour_of_day = date_range.hour.values
    day_of_week = date_range.dayofweek.values
    
    # 1. OUTDOOR TEMPERATURE (Seasonal + Daily cycle)
    # Base temperature with seasonal variation and daily fluctuations
    base_outdoor_temp = 20 + 8 * np.sin((hour_of_day - 10) * np.pi / 12)
    seasonal_offset = 5 * np.sin(np.arange(n) * 2 * np.pi / (30 * 24))  # 30-day cycle
    outdoor_temp = base_outdoor_temp + seasonal_offset + np.random.normal(0, 2, n)
    
    # 2. BASE ENERGY LOAD (Simulate daily cycles)
    # Buildings use more power during the day (8am-6pm)
    base_load = 50 + 50 * np.sin((hour_of_day - 6) * np.pi / 12)**2
    
    # 3. WEEKEND REDUCTION (60% lower on weekends)
    is_weekend = day_of_week >= 5
    base_load[is_weekend] *= 0.4
    
    # 4. INDOOR TEMPERATURE (Controlled by HVAC)
    # Target ~22°C, HVAC works to maintain it
    hvac_effort = np.where(outdoor_temp > 22, (outdoor_temp - 22) * 0.3, (22 - outdoor_temp) * 0.2)
    indoor_temp = 22 + hvac_effort + np.random.normal(0, 0.5, n)  # Tight control
    
    # 5. OCCUPANCY (People count)
    # Peak occupancy 8am-6pm on weekdays, minimal at night/weekends
    is_business_hours = (hour_of_day >= 8) & (hour_of_day <= 18)
    is_weekday = day_of_week < 5
    base_occupancy = np.where(is_business_hours & is_weekday, 
                              np.random.uniform(300, 500, n), 
                              np.random.uniform(10, 50, n))
    occupancy = base_occupancy + np.random.normal(0, 20, n)
    occupancy = np.clip(occupancy, 0, 600)  # Cap at 600 people
    
    # 6. HUMIDITY (%)
    # Higher in hot/cold weather, controlled indoors
    base_humidity = 50 - 10 * np.sin((hour_of_day - 6) * np.pi / 12)  # Daily cycle
    humidity_effect = -0.5 * np.abs(outdoor_temp - 20)  # Higher when extreme temps
    humidity = base_humidity + humidity_effect + np.random.normal(0, 5, n)
    humidity = np.clip(humidity, 25, 75)
    
    # 7. HVAC STATUS (ON/OFF)
    # ON when building occupied or extreme temps
    needs_heating = outdoor_temp < 18
    needs_cooling = outdoor_temp > 24
    hvac_status = ((occupancy > 100) | needs_heating | needs_cooling).astype(int)
    
    # 8. SOLAR IRRADIANCE (W/m²)
    # 0 at night, peaks at noon, affected by clouds
    is_daytime = (hour_of_day >= 6) & (hour_of_day <= 20)
    solar_peak = 800 * np.sin((hour_of_day - 6) * np.pi / 14)**2
    cloud_cover = np.random.uniform(0.3, 1.0, n)  # Random cloudiness
    solar_irradiance = np.where(is_daytime, solar_peak * cloud_cover, 0)
    
    # 9. WIND SPEED (km/h)
    # Random with occasional storms
    base_wind = np.random.gamma(2, 3, n)  # Mostly low wind
    storm_events = np.random.choice([0, 1], n, p=[0.95, 0.05])  # 5% chance of storm
    wind_speed = base_wind + storm_events * np.random.uniform(15, 25, n)
    wind_speed = np.clip(wind_speed, 0, 40)
    
    # 10. SETPOINT TEMPERATURE (°C)
    # 22°C for cooling, 20°C for heating based on outdoor temp
    setpoint_temp = np.where(outdoor_temp > 20, 22.0, 20.0)
    
    # 11. EQUIPMENT AGE (years)
    # Fixed at 5 years for consistency
    equipment_age = np.full(n, 5.0)
    
    # 12. DAY TYPE
    # Weekday, Weekend, or Holiday (random 10% holidays on weekdays)
    day_type = np.where(is_weekend, 'Weekend', 'Weekday')
    holiday_indices = np.random.choice(np.where(is_weekday)[0], size=int(np.sum(is_weekday) * 0.1), replace=False)
    day_type[holiday_indices] = 'Holiday'
    
    # 13. NOISE AND ANOMALIES
    noise = np.random.normal(0, 5, n)
    anomalies = np.zeros(n)
    indices = np.random.choice(np.arange(n), size=15, replace=False)
    anomalies[indices] = np.random.uniform(50, 100, size=15)
    
    # Calculate total energy with all factors
    # Energy increases with occupancy, HVAC needs, and outdoor temp extremes
    occupancy_load = occupancy * 0.05  # People add heat load
    hvac_extra = np.where(hvac_status == 1, np.abs(outdoor_temp - 22) * 2, 0)
    total_load = base_load + occupancy_load + hvac_extra + noise + anomalies
    
    # Create DataFrame with all variables
    df = pd.DataFrame({
        'timestamp': date_range,
        'energy_kwh': total_load,
        'outdoor_temp': outdoor_temp,
        'indoor_temp': indoor_temp,
        'occupancy': occupancy.astype(int),
        'humidity': humidity.round(1),
        'hvac_status': hvac_status,
        'solar_irradiance': solar_irradiance.round(1),
        'wind_speed': wind_speed.round(1),
        'building_zone': 'Main Building',
        'setpoint_temp': setpoint_temp,
        'equipment_age': equipment_age,
        'day_type': day_type
    })
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Save
    df.to_csv('data/building_data.csv', index=False)
    print(f"Generated {n} hours of realistic building data")
    print(f"Variables: {list(df.columns)}")
    print(f"Anomalies injected: {len(indices)} points")
    print("Data saved to data/building_data.csv")

if __name__ == "__main__":
    generate_building_data()
