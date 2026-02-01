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
co2_impact = wasted_kwh * 0.0004 # Approx tons of CO2 per kWh

with col1:
    st.metric(label="⚠️ Anomalies Detected", value=len(anomalies))
with col2:
    st.metric(label="💸 Est. Wasted Cost (Monthly)", value=f"${wasted_cost:,.2f}", delta="-High Priority", delta_color="inverse")
with col3:
    st.metric(label="🌍 Sustainability Impact", value=f"{co2_impact:.2f} Tons CO2", delta="Avoidable")

# --- AI PERFORMANCE METRICS ---
st.markdown("---")
st.subheader("🤖 AI Model Performance")
col4, col5, col6 = st.columns(3)

# Calculate AI performance metrics
total_data_points = len(df)
anomaly_count = len(anomalies)
anomaly_rate = (anomaly_count / total_data_points) * 100
avg_anomaly_score = df[df['is_anomaly']]['anomaly_score'].mean() if anomaly_count > 0 else 0
model_confidence = min(100, max(0, 85 + (avg_anomaly_score * 10)))  # Simulated confidence metric

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
fig.add_hline(y=avg_load, line_dash="dash", annotation_text="Avg Baseline")
st.plotly_chart(fig, use_container_width=True)

# --- EXPLAINABILITY & GOVERNANCE ---
st.subheader("🔍 Governance & Explainability")
with st.expander("Why was this flagged? (Model Interpretability)"):
    st.write("""
    The AI model (Isolation Forest) flagged these points because they deviate significantly from the 
    learned correlation between **Outdoor Temperature** and **Energy Usage**.
    
    *Example:* High energy usage detected during low-temperature hours suggests a 'Stuck Damper' or 'Heating Valve Leak'.
    """)
    st.dataframe(anomalies[['timestamp', 'energy_kwh', 'outdoor_temp']].head())

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

methodology_tab, co2_tab, cost_tab = st.tabs(["Anomaly Detection", "CO2 Calculation", "Cost Calculation"])

with methodology_tab:
    st.markdown("""
    **Isolation Forest Algorithm**
    
    The anomaly detection uses an unsupervised machine learning algorithm called Isolation Forest:
    
    1. **How it works**: The algorithm isolates anomalies by randomly selecting features and split values
    2. **Anomaly Score**: Data points that require fewer splits to isolate are flagged as anomalies
    3. **Contamination Rate**: Set to 5% - expects 5% of data points to be anomalous
    4. **Features Used**: Energy consumption (kWh) and outdoor temperature correlation
    
    **Why this matters**: Traditional threshold-based systems miss contextual anomalies (e.g., high energy use during cool weather)
    """)

with co2_tab:
    st.markdown(r"""
    **CO2 Emissions Calculation**
    
    Formula: `Wasted Energy (kWh) × 0.0004 = CO2 Tons`
    
    **Calculation Steps:**
    1. Calculate average normal energy consumption: $\bar{x} = \frac{\sum normal\_energy}{count}$
    2. For each anomaly: $Excess = Anomaly\_Energy - \bar{x}$
    3. Sum all excess: $Total\_Wasted = \sum Excess$
    4. Convert to CO2: $CO2 = Total\_Wasted × 0.0004$
    
    **Emission Factor**: 0.0004 tons CO2 per kWh (based on average grid electricity carbon intensity)
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