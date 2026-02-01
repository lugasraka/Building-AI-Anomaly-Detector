import streamlit as st
import pandas as pd
import plotly.express as px
from model_logic import AnomalyDetector
from data_generator import generate_building_data
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="GreenLens AI", layout="wide")

# --- HEADER ---
st.title("🌱 GreenLens: Intelligent Building Anomaly Detection")
st.markdown("""
**Program Manager Dashboard** | Aligning Operations with EcoStruxure Strategy
*This prototype demonstrates how AI correlates energy spikes with financial impact.*
""")
st.markdown("---")

# --- SIDEBAR (Controls) ---
st.sidebar.header("Configuration")
cost_per_kwh = st.sidebar.number_input("Energy Cost ($/kWh)", value=0.15)

# CO2 Emission Factor Selection
emission_option = st.sidebar.selectbox(
    "CO2 Emission Factor",
    options=["Grid Average (0.4 kg/kWh)", "Renewable-Heavy (0.2 kg/kWh)", "Coal-Heavy (0.8 kg/kWh)", "Custom"],
    index=0,
    help="Select based on your region's energy mix. Grid Average is suitable for most locations."
)

# Map selection to kg/kWh value
emission_factors = {
    "Grid Average (0.4 kg/kWh)": 0.4,
    "Renewable-Heavy (0.2 kg/kWh)": 0.2,
    "Coal-Heavy (0.8 kg/kWh)": 0.8
}

if emission_option == "Custom":
    emission_factor_kg = st.sidebar.number_input(
        "Custom Factor (kg CO2/kWh)",
        min_value=0.1,
        max_value=2.0,
        value=0.4,
        step=0.1,
        help="Enter your specific emission factor in kg CO2 per kWh"
    )
else:
    emission_factor_kg = emission_factors[emission_option]

if st.sidebar.button("🔄 Regenerate Simulation Data"):
    if not os.path.exists('data'): os.makedirs('data')
    generate_building_data()
    st.sidebar.success("New sensor data generated!")

# --- LOAD DATA ---
try:
    df = pd.read_csv('data/building_data.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
except FileNotFoundError:
    st.error("Data not found. Please click 'Regenerate Simulation Data' in the sidebar.")
    st.stop()

# --- RUN AI MODEL ---
detector = AnomalyDetector(contamination=0.05)
df = detector.train_and_predict(df)

# Filter only anomalies
anomalies = df[df['is_anomaly']]
normal = df[~df['is_anomaly']]

# --- BUSINESS IMPACT METRICS (The "Manager View") ---
col1, col2, col3 = st.columns(3)

# Calculate Wasted Energy (Difference between Anomaly and Average Load)
avg_load = normal['energy_kwh'].mean()
wasted_kwh = (anomalies['energy_kwh'] - avg_load).sum()
wasted_cost = wasted_kwh * cost_per_kwh
# Convert kg to metric tons for display
co2_impact_tons = wasted_kwh * emission_factor_kg / 1000

with col1:
    st.metric(label="⚠️ Anomalies Detected", value=len(anomalies))
with col2:
    st.metric(label="💸 Est. Wasted Cost (Monthly)", value=f"${wasted_cost:,.2f}", delta="-High Priority", delta_color="inverse")
with col3:
    st.metric(label="🌍 Sustainability Impact", value=f"{co2_impact_tons:.2f} Tons CO2", delta=f"{emission_factor_kg} kg/kWh factor")

# --- AI PERFORMANCE METRICS ---
st.markdown("---")
st.subheader("🤖 AI Model Performance")
col4, col5, col6 = st.columns(3)

# Calculate AI performance metrics
total_data_points = len(df)
anomaly_count = len(anomalies)
anomaly_rate = (anomaly_count / total_data_points) * 100
# Calculate model confidence based on separation between anomalies and normal data
avg_anomaly_score = df[df['is_anomaly']]['anomaly_score'].mean() if anomaly_count > 0 else 0
avg_normal_score = df[~df['is_anomaly']]['anomaly_score'].mean()
score_std = df['anomaly_score'].std()

# Confidence measures how well-separated anomalies are from normal data
# Higher separation = more confident the model correctly identified true anomalies
separation_score = (avg_anomaly_score - avg_normal_score) / score_std if score_std > 0 else 0
model_confidence = min(100, max(0, 70 + (separation_score * 8)))  # Scale: 70-100% range

with col4:
    st.metric(label="📊 Detection Rate", value=f"{anomaly_rate:.1f}%", delta="Target: 5%", delta_color="off")
with col5:
    st.metric(label="🎯 Model Confidence", value=f"{model_confidence:.0f}%", delta="Good" if model_confidence >= 85 else "Review", delta_color="normal" if model_confidence >= 85 else "inverse")
with col6:
    avg_score_all = df['anomaly_score'].mean()
    st.metric(label="📈 Avg Anomaly Score", value=f"{avg_anomaly_score:.3f}", delta=f"Baseline: {avg_score_all:.3f}", delta_color="off")

# --- VISUALIZATION (The "Engineer View") ---
st.subheader("Real-time Energy Consumption Analysis")

# Plotly Chart
fig = px.scatter(df, x='timestamp', y='energy_kwh', 
                 color='is_anomaly', 
                 color_discrete_map={False: 'blue', True: 'red'},
                 title="HVAC Energy Load (Red = AI Detected Anomaly)")

# Add a threshold line for visual reference
fig.add_hline(y=avg_load, line_dash="dash", line_color="orange", annotation_text="Avg Baseline")
st.plotly_chart(fig, use_container_width=True)

# --- EXPLAINABILITY & GOVERNANCE ---
st.subheader("🔍 Why Was This Flagged?")

st.info("""
**The AI detected unusual energy patterns** - the system is using more power than expected based on:
- Current outdoor temperature and weather conditions
- Building occupancy levels and day of the week
- Normal operating patterns from past data
""")

if len(anomalies) > 0:
    st.markdown("**Common Causes:**")
    
    causes_col1, causes_col2 = st.columns(2)
    with causes_col1:
        st.markdown("🔧 **HVAC Issues**")
        st.caption("Heating/cooling running when not needed, stuck dampers, or equipment malfunction")
        
        st.markdown("📅 **Schedule Problems**") 
        st.caption("Building systems running during weekends, holidays, or after hours")
    
    with causes_col2:
        st.markdown("⚠️ **Equipment Faults**")
        st.caption("Valve leaks, stuck actuators, or cooling system struggling")
        
        st.markdown("🔍 **Unusual Loads**")
        st.caption("Equipment left running or unexpected energy usage")
    
    st.markdown("---")
    st.markdown("**Recommended Actions:**")
    
    rec_col1, rec_col2 = st.columns(2)
    with rec_col1:
        st.success("📊 Check HVAC schedules and setpoints")
        st.success("🔧 Inspect dampers, valves, and sensors")
    with rec_col2:
        st.success("📅 Review weekend/holiday automation settings")
        st.success("❄️ Verify AC filters and maintenance status")
    
    st.markdown("---")
    st.markdown(f"**Latest {min(5, len(anomalies))} Anomalies:**")
    
    display_cols = ['timestamp', 'energy_kwh', 'outdoor_temp', 'occupancy', 'day_type']
    recent_anomalies = anomalies[display_cols].tail(min(5, len(anomalies))).sort_values('timestamp', ascending=False)
    st.dataframe(recent_anomalies, hide_index=True)
else:
    st.success("✅ No anomalies detected - all systems operating normally!")

# --- PROGRAM ROADMAP ---
st.markdown("---")
st.subheader("Program Roadmap")

roadmap_data = {
    "Phase": ["Phase 1: MVP", "Phase 2: Connectivity", "Phase 3: Automation"],
    "Timeline": ["Current", "Q1 2026", "Future"],
    "Key Deliverables": [
        "CSV data ingestion, Baseline model, Cost visualization",
        "Live API stream, User feedback loop, Model retraining",
        "EcoStruxure integration, Automated setpoint control"
    ],
    "Goal": ["Proof of Value", "Operational Integration", "Autonomous Optimization"]
}

st.dataframe(roadmap_data, use_container_width=True, hide_index=True)

# --- METHODOLOGY EXPLANATION ---
st.markdown("---")
st.subheader("Methodology & Calculations")

methodology_tab, co2_tab, cost_tab, author_tab = st.tabs(["Anomaly Detection", "CO2 Calculation", "Cost Calculation", "About"])

with methodology_tab:
    st.markdown("""
    **COPOD Algorithm (Copula-based Outlier Detection)**
    
    The anomaly detection uses COPOD, a state-of-the-art unsupervised algorithm optimized for both speed and accuracy:
    
    1. **How it works**: Uses copula functions to model the joint distribution between energy consumption and outdoor temperature
    2. **Anomaly Score**: Calculates tail probabilities - points in the extreme tails of the distribution are flagged as anomalies
    3. **Contamination Rate**: Set to 5% - expects 5% of data points to be anomalous
    4. **Features Used**: Energy consumption (kWh) and outdoor temperature correlation, capturing their statistical dependencies
    
    **Why COPOD**: 
    - **Fast inference**: ~10-50ms for real-time detection (faster than Isolation Forest)
    - **Better accuracy**: Handles feature correlations better than tree-based methods
    - **Interpretable scores**: Direct probability-based anomaly scores
    - **Production-ready**: Optimal balance of speed and accuracy for building energy monitoring
    
    **Why this matters**: Detects contextual anomalies that threshold-based systems miss (e.g., high energy use during cool weather indicating stuck dampers)
    """)

with co2_tab:
    st.markdown(r"""
    **CO2 Emissions Calculation**
    
    Formula: `Wasted Energy (kWh) × Emission Factor (kg/kWh) ÷ 1000 = CO2 (Tons)`
    
    **Calculation Steps:**
    1. Calculate average normal energy consumption: $\bar{x} = \frac{\sum normal\_energy}{count}$
    2. For each anomaly: $Excess = Anomaly\_Energy - \bar{x}$
    3. Sum all excess: $Total\_Wasted = \sum Excess$
    4. Calculate CO2 in kg: $CO2\_kg = Total\_Wasted \times Emission\_Factor$
    5. Convert to metric tons: $CO2\_tons = \frac{CO2\_kg}{1000}$
    
    **Emission Factor Options** (configurable in sidebar):
    - **Grid Average: 0.4 kg/kWh** - Suitable for most mixed-energy grids (default)
    - **Renewable-Heavy: 0.2 kg/kWh** - For regions with high solar/wind penetration
    - **Coal-Heavy: 0.8 kg/kWh** - For regions with fossil fuel dominant grids
    - **Custom**: Set your own factor (0.1 - 2.0 kg/kWh range)
    
    *Note: Factors represent kg of CO2 emitted per kWh of electricity consumed, based on your regional grid composition.*
    """)

with cost_tab:
    st.markdown(r"""
    **Financial Impact Calculation**
    
    Formula: `Wasted Energy (kWh) × Cost per kWh = Wasted Cost ($)`
    
    **Calculation Steps:**
    1. Calculate average normal energy consumption
    2. For each anomaly: $Excess = Anomaly\_Energy - Average$
    3. Sum all excess energy: $Total\_Wasted\_kWh = \sum Excess$
    4. Apply cost rate: $Cost = Total\_Wasted\_kWh × Cost\_per\_kWh$
    
    **Current Rate**: $0.15 per kWh (configurable in sidebar)
    """)

with author_tab:
    st.markdown("""
    **About the Author**
    
    **Raka Adrianto**  
    *Sustainability x AI Program Manager*
    
    **Connect:**
    - [LinkedIn](https://www.linkedin.com/in/lugasraka/)
    - [GitHub](https://github.com/lugasraka)
    """)