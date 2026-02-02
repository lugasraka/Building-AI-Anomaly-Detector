"""
MLOps Monitoring Dashboard for GreenLens AI
Provides real-time visibility into model health, drift, and performance
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mlops.monitoring import MonitoringDashboard, DriftDetector, PerformanceTracker
from mlops.model_registry import ModelRegistry
from model_logic import AnomalyDetector
from data_generator import generate_building_data

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="GreenLens AI - MLOps Monitoring",
    page_icon="🔬",
    layout="wide"
)

# --- HEADER ---
st.title("🔬 MLOps Monitoring Dashboard")
st.markdown("""
**Model Operations & Health Monitoring** | Ensuring Production AI Reliability
*Real-time visibility into model performance, data drift, and system health*
""")
st.markdown("---")

# Initialize monitoring components
monitoring = MonitoringDashboard()
registry = ModelRegistry()

# --- SIDEBAR ---
st.sidebar.header("⚙️ Monitoring Controls")

# Time range selection
time_range = st.sidebar.selectbox(
    "Performance Time Range",
    options=["Last 1 Hour", "Last 6 Hours", "Last 24 Hours", "Last 7 Days"],
    index=2
)

time_hours = {"Last 1 Hour": 1, "Last 6 Hours": 6, "Last 24 Hours": 24, "Last 7 Days": 168}[time_range]

# Model version info
st.sidebar.markdown("---")
st.sidebar.subheader("📦 Model Registry")

model_history = registry.get_model_history()
if model_history:
    current_model_id = registry.registry.get("current_version", "None")
    st.sidebar.info(f"**Current Model:** `{current_model_id[:20]}...`")
    st.sidebar.text(f"Total Versions: {len(model_history)}")
    
    # Show recent versions
    recent_versions = model_history[:3]
    for model in recent_versions:
        status = "🟢 Active" if model["model_id"] == current_model_id else "⚪ Inactive"
        st.sidebar.caption(f"{status} {model['version']} ({model['created_at'][:10]})")
else:
    st.sidebar.warning("No models registered yet")

# --- MAIN DASHBOARD ---

# Load current data
try:
    df = pd.read_csv('data/building_data.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
except FileNotFoundError:
    st.error("No data found. Please generate data from the main dashboard first.")
    st.stop()

# Run model to get predictions (for monitoring)
detector = AnomalyDetector(contamination=0.05)
df = detector.train_and_predict(df)

# Get health status
features = ['energy_kwh', 'outdoor_temp']
health_status = monitoring.get_health_status(df, features)

# --- TOP METRICS ROW ---
st.subheader("🎯 System Health Overview")

col1, col2, col3, col4 = st.columns(4)

# Health Status Indicator
with col1:
    status = health_status["status"]
    if status == "healthy":
        st.metric("🟢 System Health", "HEALTHY", delta="All Good")
    elif status == "warning":
        st.metric("🟡 System Health", "WARNING", delta="Action Needed", delta_color="off")
    else:
        st.metric("🔴 System Health", "CRITICAL", delta="Immediate Action", delta_color="inverse")

# Drift Status
with col2:
    drift_detected = health_status["drift_status"].get("drift_detected", False)
    drift_score = health_status["drift_status"].get("overall_drift_score", 0)
    if drift_detected:
        st.metric("📊 Data Drift", f"{drift_score:.3f}", delta="Drift Detected", delta_color="inverse")
    else:
        st.metric("📊 Data Drift", f"{drift_score:.3f}", delta="Stable")

# Performance Status
perf_status = health_status["performance_status"]
with col3:
    if isinstance(perf_status, dict) and "latency_stats" in perf_status:
        latency = perf_status["latency_stats"]["mean_ms"]
        st.metric("⚡ Avg Latency", f"{latency:.1f}ms", delta="Target: <50ms")
    else:
        st.metric("⚡ Avg Latency", "N/A", delta="No data")

with col4:
    if isinstance(perf_status, dict):
        pred_count = perf_status.get("total_predictions", 0)
        st.metric("📈 Predictions", f"{pred_count}", delta=f"Last {time_hours}h")
    else:
        st.metric("📈 Predictions", "N/A")

# --- ALERTS & RECOMMENDATIONS ---
if health_status["issues"]:
    st.warning("⚠️ **Issues Detected:**")
    for issue in health_status["issues"]:
        st.markdown(f"- {issue}")

if health_status["recommendations"]:
    with st.expander("💡 **Recommendations**", expanded=True):
        for rec in health_status["recommendations"]:
            st.markdown(f"✓ {rec}")

st.markdown("---")

# --- DRIFT ANALYSIS SECTION ---
st.subheader("📊 Data Drift Analysis")

drift_results = health_status["drift_status"]

if "error" in drift_results:
    st.info(drift_results["error"])
else:
    # Drift metrics table
    if drift_results.get("features"):
        drift_data = []
        for feature, stats in drift_results["features"].items():
            drift_data.append({
                "Feature": feature,
                "PSI Score": f"{stats['psi_score']:.4f}",
                "KS p-value": f"{stats['ks_pvalue']:.4f}",
                "Mean Shift": f"{stats['mean_shift_pct']:+.1f}%",
                "Status": "🔴 Drift" if stats["drift_detected"] else "🟢 Stable"
            })
        
        drift_df = pd.DataFrame(drift_data)
        st.dataframe(drift_df, use_container_width=True, hide_index=True)
        
        # Feature distribution comparison
        st.markdown("#### Feature Distribution Comparison")
        
        # Load reference stats for visualization
        ref_stats = monitoring.drift_detector.load_reference_stats()
        if ref_stats:
            feature_to_plot = st.selectbox("Select Feature to Analyze", features)
            
            if feature_to_plot in drift_results["features"]:
                # Create comparison chart
                fig = go.Figure()
                
                # Current data histogram
                current_values = df[feature_to_plot].dropna()
                fig.add_trace(go.Histogram(
                    x=current_values,
                    name='Current Data',
                    opacity=0.7,
                    nbinsx=20
                ))
                
                # Reference mean line
                ref_mean = ref_stats["features"][feature_to_plot]["mean"]
                fig.add_vline(
                    x=ref_mean, 
                    line_dash="dash", 
                    line_color="red",
                    annotation_text=f"Reference Mean: {ref_mean:.2f}"
                )
                
                # Current mean line
                current_mean = current_values.mean()
                fig.add_vline(
                    x=current_mean,
                    line_dash="dash",
                    line_color="blue",
                    annotation_text=f"Current Mean: {current_mean:.2f}"
                )
                
                fig.update_layout(
                    title=f"Distribution: {feature_to_plot}",
                    xaxis_title=feature_to_plot,
                    yaxis_title="Count",
                    barmode='overlay'
                )
                
                st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- PERFORMANCE METRICS SECTION ---
st.subheader("⚡ Model Performance Metrics")

perf_summary = monitoring.performance_tracker.get_performance_summary(hours=time_hours)

if isinstance(perf_summary, dict) and "error" not in perf_summary:
    # Performance metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Predictions", perf_summary["total_predictions"])
        st.metric("Anomalies Detected", perf_summary["anomaly_count"])
    
    with col2:
        latency_stats = perf_summary["latency_stats"]
        st.metric("Mean Latency", f"{latency_stats['mean_ms']:.1f}ms")
        st.metric("P95 Latency", f"{latency_stats['p95_ms']:.1f}ms")
    
    with col3:
        st.metric("Anomaly Rate", f"{perf_summary['anomaly_rate']:.2f}%")
        st.metric("P99 Latency", f"{latency_stats['p99_ms']:.1f}ms")
    
    # Performance trends
    st.markdown("#### Performance Trends")
    trends = monitoring.performance_tracker.get_prediction_trend(hours=time_hours, interval_minutes=60)
    
    if trends:
        trend_df = pd.DataFrame(trends)
        trend_df['interval_start'] = pd.to_datetime(trend_df['interval_start'])
        
        # Create subplots
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=('Prediction Volume & Anomalies', 'Latency Trends'),
            vertical_spacing=0.15
        )
        
        # Top plot: Predictions and anomalies
        fig.add_trace(
            go.Scatter(
                x=trend_df['interval_start'], 
                y=trend_df['prediction_count'],
                name='Predictions',
                mode='lines+markers'
            ),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Scatter(
                x=trend_df['interval_start'],
                y=trend_df['anomaly_count'],
                name='Anomalies',
                mode='lines+markers',
                line=dict(color='red')
            ),
            row=1, col=1
        )
        
        # Bottom plot: Latency
        fig.add_trace(
            go.Scatter(
                x=trend_df['interval_start'],
                y=trend_df['avg_latency_ms'],
                name='Avg Latency (ms)',
                mode='lines+markers',
                line=dict(color='green')
            ),
            row=2, col=1
        )
        
        fig.update_layout(height=600, showlegend=True)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No trend data available. Predictions will be logged going forward.")
else:
    st.info("No performance data available yet. Start making predictions to populate metrics.")

st.markdown("---")

# --- MODEL VERSION HISTORY ---
st.subheader("📦 Model Version History")

if model_history:
    # Create version comparison table
    version_data = []
    for model in model_history:
        perf = model.get("performance_metrics", {})
        version_data.append({
            "Version": model["version"],
            "Created": model["created_at"][:16],
            "Status": "🟢 Active" if model["model_id"] == current_model_id else "⚪ Inactive",
            "Latency (ms)": f"{perf.get('latency_ms', 'N/A')}",
            "Confidence": f"{perf.get('confidence', 'N/A')}%",
            "Description": model.get("description", "")[:50]
        })
    
    version_df = pd.DataFrame(version_data)
    st.dataframe(version_df, use_container_width=True, hide_index=True)
    
    # Version comparison (if multiple versions exist)
    if len(model_history) >= 2:
        st.markdown("#### Version Comparison")
        
        col1, col2 = st.columns(2)
        with col1:
            model_1 = st.selectbox(
                "Compare Version A",
                options=[m["model_id"] for m in model_history],
                format_func=lambda x: next((m["version"] for m in model_history if m["model_id"] == x), x)[:10]
            )
        
        with col2:
            model_2 = st.selectbox(
                "Compare Version B",
                options=[m["model_id"] for m in model_history],
                format_func=lambda x: next((m["version"] for m in model_history if m["model_id"] == x), x)[:10],
                index=1 if len(model_history) > 1 else 0
            )
        
        if st.button("🔍 Compare Versions"):
            comparison = registry.compare_versions(model_1, model_2)
            
            if "error" not in comparison:
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"**{comparison['model_1']['version']}**")
                    st.text(f"Created: {comparison['model_1']['created_at'][:10]}")
                    metrics_1 = comparison['model_1']['metrics']
                    st.metric("Latency", f"{metrics_1.get('latency_ms', 0):.1f}ms")
                    st.metric("Confidence", f"{metrics_1.get('confidence', 0):.0f}%")
                
                with col2:
                    st.markdown(f"**{comparison['model_2']['version']}**")
                    st.text(f"Created: {comparison['model_2']['created_at'][:10]}")
                    metrics_2 = comparison['model_2']['metrics']
                    
                    # Show deltas
                    lat_diff = comparison['comparison']['latency_diff']
                    conf_diff = comparison['comparison']['confidence_diff']
                    
                    st.metric(
                        "Latency", 
                        f"{metrics_2.get('latency_ms', 0):.1f}ms",
                        delta=f"{lat_diff:+.1f}ms",
                        delta_color="inverse" if lat_diff > 0 else "normal"
                    )
                    st.metric(
                        "Confidence",
                        f"{metrics_2.get('confidence', 0):.0f}%",
                        delta=f"{conf_diff:+.0f}%",
                        delta_color="normal" if conf_diff > 0 else "inverse"
                    )
else:
    st.info("No model versions registered. Train a model from the main dashboard to begin tracking.")

st.markdown("---")

# --- FOOTER ---
st.caption("MLOps Monitoring Dashboard | GreenLens AI v1.0 | Model Registry & Drift Detection Active")
