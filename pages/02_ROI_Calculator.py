"""
Interactive ROI Calculator for GreenLens AI
Helps customers understand financial returns and business value
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from fpdf import FPDF
import io
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="GreenLens AI - ROI Calculator",
    page_icon="💰",
    layout="wide"
)

# --- HEADER ---
st.title("💰 GreenLens AI - ROI Calculator")
st.markdown("""
**Business Value Assessment Tool** | Calculate Your Return on Investment
*Interactive calculator to estimate energy savings, cost avoidance, and payback period*
""")
st.markdown("---")

# --- SIDEBAR INPUTS ---
st.sidebar.header("🏢 Building Portfolio")

# Building characteristics
num_buildings = st.sidebar.number_input("Number of Buildings", min_value=1, max_value=500, value=10)
total_sqft = st.sidebar.number_input("Total Square Footage (sq ft)", min_value=1000, max_value=10000000, value=500000)
avg_energy_cost = st.sidebar.number_input("Average Annual Energy Cost per Building ($)", min_value=10000, max_value=5000000, value=100000)

st.sidebar.markdown("---")
st.sidebar.header("⚡ Energy Profile")

# Energy waste estimation
waste_percentage = st.sidebar.slider(
    "Estimated Energy Waste (%)", 
    min_value=5, 
    max_value=35, 
    value=18,
    help="Industry average: 15-30%"
)

capture_rate = st.sidebar.slider(
    "GreenLens AI Savings Capture (% of waste)", 
    min_value=50, 
    max_value=90, 
    value=70,
    help="Typical: 60-80% of identified waste can be eliminated"
)

energy_price_inflation = st.sidebar.slider(
    "Annual Energy Price Inflation (%)", 
    min_value=0.0, 
    max_value=10.0, 
    value=3.0,
    step=0.5
)

st.sidebar.markdown("---")
st.sidebar.header("💵 Investment")

# Pricing inputs
implementation_cost = st.sidebar.number_input("Implementation Cost ($)", min_value=10000, max_value=500000, value=75000)
annual_subscription = st.sidebar.number_input("Annual Subscription per Building ($)", min_value=5000, max_value=100000, value=12000)

st.sidebar.markdown("---")
st.sidebar.header("🌍 Sustainability")

co2_factor = st.sidebar.selectbox(
    "CO2 Emission Factor",
    options=[
        "Grid Average (0.4 kg/kWh)",
        "Renewable-Heavy (0.2 kg/kWh)", 
        "Coal-Heavy (0.8 kg/kWh)",
        "Singapore Grid (0.5 kg/kWh)"
    ],
    index=0
)

emission_factors = {
    "Grid Average (0.4 kg/kWh)": 0.4,
    "Renewable-Heavy (0.2 kg/kWh)": 0.2,
    "Coal-Heavy (0.8 kg/kWh)": 0.8,
    "Singapore Grid (0.5 kg/kWh)": 0.5
}

co2_per_kwh = emission_factors[co2_factor]

st.sidebar.markdown("---")
st.sidebar.header("📊 Analysis Period")

analysis_years = st.sidebar.slider("Analysis Period (Years)", min_value=3, max_value=10, value=5)
discount_rate = st.sidebar.slider("Discount Rate (%)", min_value=0.0, max_value=15.0, value=8.0, step=0.5)

# --- CALCULATIONS ---

# Total annual energy cost
total_annual_energy = avg_energy_cost * num_buildings

# Calculate savings
waste_amount = total_annual_energy * (waste_percentage / 100)
annual_savings = waste_amount * (capture_rate / 100)

# Total annual cost
total_annual_cost = annual_subscription * num_buildings

# Year-by-year projection
years = list(range(1, analysis_years + 1))
projection_data = []

cumulative_savings = 0
cumulative_cost = implementation_cost

for year in years:
    # Apply inflation to energy cost and savings
    inflation_factor = (1 + energy_price_inflation/100) ** (year - 1)
    year_savings = annual_savings * inflation_factor
    
    # Annual costs
    year_cost = total_annual_cost if year > 1 else total_annual_cost  # First year includes implementation
    
    if year == 1:
        year_cost += implementation_cost
    
    # Net benefit
    net_benefit = year_savings - (total_annual_cost if year > 1 else total_annual_cost)
    
    # Cumulative
    cumulative_savings += year_savings
    cumulative_cost += (total_annual_cost if year > 1 else 0)
    
    # CO2 reduction
    # Assume 1 kWh = $0.12 average cost for calculation
    kwh_saved = year_savings / 0.12
    co2_saved = (kwh_saved * co2_per_kwh) / 1000  # Convert to tons
    
    projection_data.append({
        "Year": year,
        "Annual Savings ($)": year_savings,
        "Annual Cost ($)": total_annual_cost if year > 1 else implementation_cost + total_annual_cost,
        "Net Benefit ($)": net_benefit,
        "Cumulative Savings ($)": cumulative_savings,
        "Cumulative Cost ($)": cumulative_cost,
        "Cumulative Net ($)": cumulative_savings - cumulative_cost,
        "CO2 Saved (tons)": co2_saved
    })

projection_df = pd.DataFrame(projection_data)

# Calculate NPV over 3 years (consistent with 3-Year ROI display)
cash_flows_3yr = [-implementation_cost] + [(annual_savings * ((1 + energy_price_inflation/100) ** (year-1)) - total_annual_cost) for year in range(1, 4)]
r = discount_rate / 100
npv_3yr = sum([cf / ((1 + r) ** i) for i, cf in enumerate(cash_flows_3yr)])

# Also calculate 5-year NPV for reference
cash_flows_5yr = [-implementation_cost] + [(annual_savings * ((1 + energy_price_inflation/100) ** (year-1)) - total_annual_cost) for year in range(1, 6)]
npv_5yr = sum([cf / ((1 + r) ** i) for i, cf in enumerate(cash_flows_5yr)])

# Use 3-year NPV as the primary metric (consistent with 3-Year ROI)
npv = npv_3yr
cash_flows = cash_flows_3yr

# Calculate IRR manually using Newton-Raphson method (np.irr removed in NumPy 2.0+)
def calculate_irr(cash_flows, guess=0.1):
    """Calculate Internal Rate of Return using Newton-Raphson method"""
    if len(cash_flows) < 2:
        return 0
    
    def npv(rate):
        return sum([cf / ((1 + rate) ** i) for i, cf in enumerate(cash_flows)])
    
    def npv_derivative(rate):
        return sum([-i * cf / ((1 + rate) ** (i + 1)) for i, cf in enumerate(cash_flows) if i > 0])
    
    rate = guess
    for _ in range(100):  # Max iterations
        npv_val = npv(rate)
        if abs(npv_val) < 1e-6:  # Converged
            return rate
        deriv = npv_derivative(rate)
        if abs(deriv) < 1e-6:  # Avoid division by zero
            break
        rate = rate - npv_val / deriv
        if rate < -1:  # IRR can't be less than -100%
            rate = -0.99
        elif rate > 10:  # Cap at 1000%
            rate = 10
    
    return rate

irr = calculate_irr(cash_flows) * 100 if len(cash_flows) > 1 else 0

# Calculate payback period
cumulative_net = 0
payback_year = None
for i, row in projection_df.iterrows():
    cumulative_net += row["Net Benefit ($)"]
    if cumulative_net >= 0 and payback_year is None:
        payback_year = row["Year"]

# ROI calculation (3-year period for consistency with display)
total_investment_3yr = implementation_cost + (total_annual_cost * 3)
total_return_3yr = projection_df["Annual Savings ($)"].head(3).sum()
roi_percentage = ((total_return_3yr - total_investment_3yr) / total_investment_3yr) * 100

# --- MAIN DASHBOARD ---

# Top metrics row
st.subheader("📊 Executive Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Annual Savings (Year 1)", 
        f"${annual_savings:,.0f}",
        delta=f"{waste_percentage * capture_rate / 100:.1f}% reduction"
    )

with col2:
    st.metric(
        "📈 3-Year ROI", 
        f"{roi_percentage:.0f}%",
        delta=f"NPV (3Y): ${npv_3yr:,.0f}"
    )

with col3:
    payback_text = f"{payback_year} years" if payback_year else ">5 years"
    st.metric(
        "⏱️ Payback Period", 
        payback_text,
        delta="Target: <18 months" if payback_year and payback_year <= 1.5 else "Review"
    )

with col4:
    total_co2 = projection_df["CO2 Saved (tons)"].sum()
    st.metric(
        "🌍 CO2 Reduction", 
        f"{total_co2:,.0f} tons",
        delta=f"Over {analysis_years} years"
    )

st.markdown("---")

# Two column layout for detailed analysis
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("💵 Financial Projection")
    
    # Create financial projection chart
    fig = go.Figure()
    
    # Cumulative savings line
    fig.add_trace(go.Scatter(
        x=projection_df["Year"],
        y=projection_df["Cumulative Savings ($)"],
        mode='lines+markers',
        name='Cumulative Savings',
        line=dict(color='green', width=3),
        fill='tonexty'
    ))
    
    # Cumulative cost line
    fig.add_trace(go.Scatter(
        x=projection_df["Year"],
        y=projection_df["Cumulative Cost ($)"],
        mode='lines+markers',
        name='Cumulative Investment',
        line=dict(color='red', width=3)
    ))
    
    # Breakeven line
    fig.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="Breakeven")
    
    fig.update_layout(
        title="Cumulative Savings vs. Investment",
        xaxis_title="Year",
        yaxis_title="Amount ($)",
        yaxis_tickformat='$,.0f',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed projection table
    with st.expander("📋 View Detailed Projection"):
        display_df = projection_df.copy()
        for col in display_df.columns:
            if "($)" in col:
                display_df[col] = display_df[col].apply(lambda x: f"${x:,.0f}")
            elif "(tons)" in col:
                display_df[col] = display_df[col].apply(lambda x: f"{x:,.1f}")
        
        st.dataframe(display_df, use_container_width=True, hide_index=True)

with col_right:
    st.subheader("📈 Annual Cash Flow")
    
    # Cash flow chart
    fig2 = go.Figure()
    
    colors = ['red' if x < 0 else 'green' for x in projection_df["Net Benefit ($)"]]
    
    fig2.add_trace(go.Bar(
        x=projection_df["Year"],
        y=projection_df["Net Benefit ($)"],
        name='Net Benefit',
        marker_color=colors
    ))
    
    fig2.add_hline(y=0, line_dash="dash", line_color="black")
    
    fig2.update_layout(
        title="Annual Net Benefit (Savings - Costs)",
        xaxis_title="Year",
        yaxis_title="Net Benefit ($)",
        yaxis_tickformat='$,.0f',
        height=400
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    # Key metrics table
    st.markdown("#### Key Metrics")
    
    metrics_data = {
        "Metric": [
            "Total Investment (3-Year)",
            "Total Savings (3-Year)",
            "Net Benefit (3-Year)",
            "NPV 3-Year ({}% discount)".format(discount_rate),
            "NPV 5-Year ({}% discount)".format(discount_rate),
            "Average Annual Savings",
            "IRR"
        ],
        "Value": [
            f"${total_investment_3yr:,.0f}",
            f"${total_return_3yr:,.0f}",
            f"${total_return_3yr - total_investment_3yr:,.0f}",
            f"${npv_3yr:,.0f}",
            f"${npv_5yr:,.0f}",
            f"${projection_df['Annual Savings ($)'].mean():,.0f}",
            f"{irr:.1f}%"
        ]
    }
    
    metrics_df = pd.DataFrame(metrics_data)
    st.dataframe(metrics_df, use_container_width=True, hide_index=True)

st.markdown("---")

# Scenario comparison
st.subheader("🎯 Scenario Comparison")

# Create scenarios
scenarios = {
    "Conservative": {
        "waste": 12,
        "capture": 60,
        "inflation": 2.0
    },
    "Expected (Current)": {
        "waste": waste_percentage,
        "capture": capture_rate,
        "inflation": energy_price_inflation
    },
    "Optimistic": {
        "waste": 25,
        "capture": 80,
        "inflation": 4.0
    }
}

scenario_results = []

for scenario_name, params in scenarios.items():
    # Calculate savings
    waste_amt = total_annual_energy * (params["waste"] / 100)
    annual_sav = waste_amt * (params["capture"] / 100)
    
    # Calculate 3-year totals
    total_sav_3yr = sum([annual_sav * ((1 + params["inflation"]/100) ** year) for year in range(3)])
    total_cost_3yr = implementation_cost + (total_annual_cost * 3)
    roi_3yr = ((total_sav_3yr - total_cost_3yr) / total_cost_3yr) * 100
    
    # Simple payback
    annual_net = annual_sav - total_annual_cost
    payback = implementation_cost / annual_net if annual_net > 0 else 99
    
    scenario_results.append({
        "Scenario": scenario_name,
        "Waste %": params["waste"],
        "Capture %": params["capture"],
        "Year 1 Savings": annual_sav,
        "3-Year ROI": roi_3yr,
        "Payback (years)": payback
    })

scenario_df = pd.DataFrame(scenario_results)

# Display scenario comparison
col1, col2 = st.columns([2, 1])

with col1:
    fig3 = go.Figure()
    
    fig3.add_trace(go.Bar(
        name='Year 1 Savings',
        x=scenario_df["Scenario"],
        y=scenario_df["Year 1 Savings"],
        marker_color='lightblue'
    ))
    
    fig3.add_trace(go.Scatter(
        name='3-Year ROI %',
        x=scenario_df["Scenario"],
        y=scenario_df["3-Year ROI"],
        mode='lines+markers',
        line=dict(color='red', width=3),
        yaxis='y2'
    ))
    
    fig3.update_layout(
        title="Scenario Comparison: Savings vs. ROI",
        yaxis_title="Year 1 Savings ($)",
        yaxis_tickformat='$,.0f',
        yaxis2=dict(
            title="3-Year ROI (%)",
            overlaying='y',
            side='right'
        ),
        height=400,
        legend=dict(orientation="h", yanchor="bottom", y=1.02)
    )
    
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    st.markdown("#### Scenario Details")
    
    for _, row in scenario_df.iterrows():
        with st.expander(f"{row['Scenario']}"):
            st.markdown(f"**Waste %:** {row['Waste %']}%")
            st.markdown(f"**Capture %:** {row['Capture %']}%")
            st.markdown(f"**Year 1 Savings:** ${row['Year 1 Savings']:,.0f}")
            st.markdown(f"**3-Year ROI:** {row['3-Year ROI']:.0f}%")
            st.markdown(f"**Payback:** {row['Payback (years)']:.1f} years")

st.markdown("---")

# Sensitivity analysis
st.subheader("📊 Sensitivity Analysis")

st.markdown("See how changes in key assumptions impact ROI:")

# Sensitivity to waste percentage
waste_range = range(10, 31, 2)
sensitivity_waste = []

for waste in waste_range:
    waste_amt = total_annual_energy * (waste / 100)
    annual_sav = waste_amt * (capture_rate / 100)
    total_sav_3yr = sum([annual_sav * ((1 + energy_price_inflation/100) ** year) for year in range(3)])
    total_cost_3yr = implementation_cost + (total_annual_cost * 3)
    roi = ((total_sav_3yr - total_cost_3yr) / total_cost_3yr) * 100
    sensitivity_waste.append({"Waste %": waste, "3-Year ROI": roi})

sensitivity_df = pd.DataFrame(sensitivity_waste)

fig4 = px.line(
    sensitivity_df, 
    x="Waste %", 
    y="3-Year ROI",
    title="Impact of Energy Waste % on ROI",
    markers=True
)

fig4.add_vline(x=waste_percentage, line_dash="dash", line_color="red", annotation_text="Current")

st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# Implementation roadmap
st.subheader("🗓️ Implementation Roadmap")

roadmap_data = {
    "Phase": ["Discovery", "Pilot", "Validation", "Scale", "Optimize"],
    "Timeline": ["Weeks 1-2", "Months 2-3", "Month 3", "Months 4-6", "Months 7-12"],
    "Investment": [
        f"${implementation_cost * 0.3:,.0f}",
        f"${implementation_cost * 0.4:,.0f}",
        "-",
        f"${implementation_cost * 0.3:,.0f}",
        "-"
    ],
    "Expected Savings": [
        "0%",
        "5-8%",
        "10-12%",
        "15-18%",
        "18-22%"
    ]
}

roadmap_df = pd.DataFrame(roadmap_data)
st.dataframe(roadmap_df, use_container_width=True, hide_index=True)

st.markdown("---")

# Export options
st.subheader("📄 Export Results")


def generate_pdf_report():
    """Generate a professional PDF business case report"""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Cover Page
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    pdf.set_text_color(34, 139, 34)  # Green color
    pdf.cell(0, 20, 'GreenLens AI', ln=True, align='C')
    pdf.set_font('Arial', 'B', 18)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, 'Business Case Analysis', ln=True, align='C')
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f'Generated: {datetime.now().strftime("%B %d, %Y")}', ln=True, align='C')
    pdf.ln(20)
    
    # Executive Summary
    pdf.set_font('Arial', 'B', 16)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(0, 10, 'Executive Summary', ln=True, fill=True)
    pdf.ln(5)
    
    pdf.set_font('Arial', '', 11)
    summary_items = [
        ("Portfolio Size", f"{num_buildings} buildings"),
        ("Total Square Footage", f"{total_sqft:,} sq ft"),
        ("Annual Energy Cost", f"${total_annual_energy:,.0f}"),
        ("Energy Waste", f"{waste_percentage}%"),
        ("Savings Capture", f"{capture_rate}%"),
        ("Year 1 Savings", f"${annual_savings:,.0f}"),
        ("3-Year ROI", f"{roi_percentage:.1f}%"),
        ("Payback Period", f"{payback_year:.1f} years" if payback_year else "N/A"),
        ("Total CO2 Reduction", f"{total_co2:,.0f} tons"),
    ]
    
    for label, value in summary_items:
        pdf.set_font('Arial', 'B', 11)
        pdf.cell(80, 8, label + ':', ln=False)
        pdf.set_font('Arial', '', 11)
        pdf.cell(0, 8, value, ln=True)
    pdf.ln(10)
    
    # Financial Projections - 3 Year (Primary Analysis)
    pdf.set_font('Arial', 'B', 16)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(0, 10, 'Financial Projections (3-Year Analysis)', ln=True, fill=True)
    pdf.ln(5)
    
    # Table header - 3 Year
    pdf.set_fill_color(220, 220, 220)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(20, 8, 'Year', 1, 0, 'C', True)
    pdf.cell(35, 8, 'Savings', 1, 0, 'C', True)
    pdf.cell(35, 8, 'Cost', 1, 0, 'C', True)
    pdf.cell(35, 8, 'Net Benefit', 1, 0, 'C', True)
    pdf.cell(35, 8, 'Cumulative', 1, 0, 'C', True)
    pdf.cell(40, 8, 'CO2 (tons)', 1, 1, 'C', True)
    
    # Table data - First 3 years
    pdf.set_font('Arial', '', 10)
    for _, row in projection_df.head(3).iterrows():
        pdf.cell(20, 7, str(int(row['Year'])), 1, 0, 'C')
        pdf.cell(35, 7, f"${row['Annual Savings ($)']:,.0f}", 1, 0, 'R')
        pdf.cell(35, 7, f"${row['Annual Cost ($)']:,.0f}", 1, 0, 'R')
        pdf.cell(35, 7, f"${row['Net Benefit ($)']:,.0f}", 1, 0, 'R')
        pdf.cell(35, 7, f"${row['Cumulative Net ($)']:,.0f}", 1, 0, 'R')
        pdf.cell(40, 7, f"{row['CO2 Saved (tons)']:,.1f}", 1, 1, 'R')
    pdf.ln(10)
    
    # Extended 5-Year Projection
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(0, 10, 'Extended Financial Projections (5-Year)', ln=True, fill=True)
    pdf.ln(5)
    
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 6, 'Complete 5-year projection showing long-term value accumulation:', ln=True)
    pdf.ln(3)
    
    # Table header - 5 Year
    pdf.set_fill_color(220, 220, 220)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(20, 8, 'Year', 1, 0, 'C', True)
    pdf.cell(35, 8, 'Savings', 1, 0, 'C', True)
    pdf.cell(35, 8, 'Cost', 1, 0, 'C', True)
    pdf.cell(35, 8, 'Net Benefit', 1, 0, 'C', True)
    pdf.cell(35, 8, 'Cumulative', 1, 0, 'C', True)
    pdf.cell(40, 8, 'CO2 (tons)', 1, 1, 'C', True)
    
    # Table data - All 5 years
    pdf.set_font('Arial', '', 10)
    for _, row in projection_df.iterrows():
        pdf.cell(20, 7, str(int(row['Year'])), 1, 0, 'C')
        pdf.cell(35, 7, f"${row['Annual Savings ($)']:,.0f}", 1, 0, 'R')
        pdf.cell(35, 7, f"${row['Annual Cost ($)']:,.0f}", 1, 0, 'R')
        pdf.cell(35, 7, f"${row['Net Benefit ($)']:,.0f}", 1, 0, 'R')
        pdf.cell(35, 7, f"${row['Cumulative Net ($)']:,.0f}", 1, 0, 'R')
        pdf.cell(40, 7, f"{row['CO2 Saved (tons)']:,.1f}", 1, 1, 'R')
    pdf.ln(5)
    
    # 5-Year Summary Box
    total_5yr_investment = implementation_cost + (total_annual_cost * 5)
    total_5yr_savings = projection_df["Annual Savings ($)"].sum()
    total_5yr_co2 = projection_df["CO2 Saved (tons)"].sum()
    
    pdf.set_fill_color(240, 248, 255)  # Light blue background
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 8, '5-Year Summary:', ln=True, fill=True)
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 6, f"Total Investment: ${total_5yr_investment:,.0f}", ln=True)
    pdf.cell(0, 6, f"Total Savings: ${total_5yr_savings:,.0f}", ln=True)
    pdf.cell(0, 6, f"Net Benefit: ${total_5yr_savings - total_5yr_investment:,.0f}", ln=True)
    pdf.cell(0, 6, f"Total CO2 Reduction: {total_5yr_co2:,.0f} tons", ln=True)
    pdf.cell(0, 6, f"5-Year NPV: ${npv_5yr:,.0f}", ln=True)
    pdf.ln(10)
    
    # Scenario Analysis
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(0, 10, 'Scenario Analysis', ln=True, fill=True)
    pdf.ln(5)
    
    # Scenario table header
    pdf.set_fill_color(220, 220, 220)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(35, 8, 'Scenario', 1, 0, 'C', True)
    pdf.cell(25, 8, 'Waste %', 1, 0, 'C', True)
    pdf.cell(30, 8, 'Capture %', 1, 0, 'C', True)
    pdf.cell(40, 8, 'Year 1 Savings', 1, 0, 'C', True)
    pdf.cell(30, 8, '3-Yr ROI', 1, 0, 'C', True)
    pdf.cell(30, 8, 'Payback', 1, 1, 'C', True)
    
    # Scenario data
    pdf.set_font('Arial', '', 10)
    for _, row in scenario_df.iterrows():
        pdf.cell(35, 7, row['Scenario'], 1, 0, 'L')
        pdf.cell(25, 7, f"{row['Waste %']}%", 1, 0, 'C')
        pdf.cell(30, 7, f"{row['Capture %']}%", 1, 0, 'C')
        pdf.cell(40, 7, f"${row['Year 1 Savings']:,.0f}", 1, 0, 'R')
        pdf.cell(30, 7, f"{row['3-Year ROI']:.1f}%", 1, 0, 'R')
        pdf.cell(30, 7, f"{row['Payback (years)']:.1f} yrs", 1, 1, 'R')
    pdf.ln(10)
    
    # Investment Summary
    pdf.set_font('Arial', 'B', 16)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(0, 10, 'Investment Summary', ln=True, fill=True)
    pdf.ln(5)
    
    pdf.set_font('Arial', '', 11)
    investment_items = [
        ("Implementation Cost", f"${implementation_cost:,.0f}"),
        ("Annual Subscription", f"${annual_subscription:,.0f} per building"),
        ("Total Annual Cost", f"${total_annual_cost:,.0f}"),
        ("", ""),
        ("3-Year Analysis:", ""),
        ("  Total Investment", f"${total_investment_3yr:,.0f}"),
        ("  Total Savings", f"${total_return_3yr:,.0f}"),
        ("  Net Benefit", f"${total_return_3yr - total_investment_3yr:,.0f}"),
        ("  NPV (3-Year)", f"${npv_3yr:,.0f}"),
        ("", ""),
        ("5-Year Analysis:", ""),
        ("  Total Investment", f"${implementation_cost + (total_annual_cost * 5):,.0f}"),
        ("  Total Savings", f"${projection_df['Annual Savings ($)'].sum():,.0f}"),
        ("  Net Benefit", f"${projection_df['Annual Savings ($)'].sum() - (implementation_cost + (total_annual_cost * 5)):,.0f}"),
        ("  NPV (5-Year)", f"${npv_5yr:,.0f}"),
        ("", ""),
        ("Internal Rate of Return (IRR)", f"{irr:.1f}%"),
    ]
    
    for label, value in investment_items:
        pdf.set_font('Arial', 'B', 11)
        pdf.cell(80, 8, label + ':', ln=False)
        pdf.set_font('Arial', '', 11)
        pdf.cell(0, 8, value, ln=True)
    pdf.ln(10)
    
    # Assumptions
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Key Assumptions', ln=True)
    pdf.set_font('Arial', '', 10)
    assumptions = [
        f"- Analysis Period: {analysis_years} years",
        f"- Discount Rate: {discount_rate}%",
        f"- Energy Price Inflation: {energy_price_inflation}% annually",
        f"- CO2 Emission Factor: {co2_per_kwh} kg/kWh",
        f"- Industry average energy waste: 15-30%",
        f"- Typical savings capture rate: 60-80%",
    ]
    for assumption in assumptions:
        pdf.cell(0, 6, assumption, ln=True)
    
    # Footer
    pdf.ln(20)
    pdf.set_font('Arial', 'I', 9)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 10, 'GreenLens AI Business Case Analysis | Generated by ROI Calculator', ln=True, align='C')
    pdf.cell(0, 5, 'For internal use only. Projections based on user inputs and industry averages.', ln=True, align='C')
    
    return bytes(pdf.output(dest='S'))


col1, col2 = st.columns(2)

with col1:
    if st.button("📊 Generate Business Case PDF"):
        try:
            pdf_bytes = generate_pdf_report()
            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_bytes,
                file_name=f"GreenLens_AI_Business_Case_{datetime.now().strftime('%Y%m%d')}.pdf",
                mime="application/pdf"
            )
            st.success("✅ PDF report generated successfully!")
        except Exception as e:
            st.error(f"❌ Error generating PDF: {str(e)}")

with col2:
    if st.button("📈 Export to Excel"):
        try:
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                # Financial Projection sheet
                projection_df.to_excel(writer, sheet_name='Financial Projection', index=False)
                
                # Scenario Analysis sheet
                scenario_df.to_excel(writer, sheet_name='Scenario Analysis', index=False)
                
                # Sensitivity Analysis sheet
                sensitivity_df.to_excel(writer, sheet_name='Sensitivity Analysis', index=False)
                
                # Summary sheet with formatting
                summary_data = {
                    'Metric': [
                        'Report Generated',
                        'Number of Buildings',
                        'Total Square Footage (sq ft)',
                        'Average Annual Energy Cost per Building ($)',
                        'Total Annual Energy Cost ($)',
                        'Waste Percentage (%)',
                        'Capture Rate (%)',
                        'Implementation Cost ($)',
                        'Annual Subscription per Building ($)',
                        'Total Annual Subscription ($)',
                        'Year 1 Savings ($)',
                        '3-Year ROI (%)',
                        'Payback Period (years)',
                        'Total CO2 Reduction (tons)',
                        'Total 3-Year Investment ($)',
                        'Total 3-Year Savings ($)',
                        'Net Benefit 3-Year ($)',
                        'Internal Rate of Return - IRR (%)',
                        'Net Present Value - NPV ($)',
                        'Analysis Period (years)',
                        'Discount Rate (%)',
                        'Energy Price Inflation (%)',
                        'CO2 Emission Factor (kg/kWh)',
                    ],
                    'Value': [
                        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        num_buildings,
                        total_sqft,
                        f"${avg_energy_cost:,.0f}",
                        f"${total_annual_energy:,.0f}",
                        f"{waste_percentage}%",
                        f"{capture_rate}%",
                        f"${implementation_cost:,.0f}",
                        f"${annual_subscription:,.0f}",
                        f"${total_annual_cost:,.0f}",
                        f"${annual_savings:,.0f}",
                        f"{roi_percentage:.1f}%",
                        f"{payback_year:.1f}" if payback_year else "N/A",
                        f"{total_co2:,.1f}",
                        f"${total_investment_3yr:,.0f}",
                        f"${total_return_3yr:,.0f}",
                        f"${total_return_3yr - total_investment_3yr:,.0f}",
                        f"{irr:.1f}%",
                        f"${npv:,.0f}",
                        analysis_years,
                        f"{discount_rate}%",
                        f"{energy_price_inflation}%",
                        co2_per_kwh,
                    ]
                }
                pd.DataFrame(summary_data).to_excel(writer, sheet_name='Executive Summary', index=False)
                
                # Get workbook and apply formatting
                workbook = writer.book
                for sheet_name in writer.sheets:
                    worksheet = writer.sheets[sheet_name]
                    # Auto-adjust column widths
                    for column in worksheet.columns:
                        max_length = 0
                        column_letter = column[0].column_letter
                        for cell in column:
                            try:
                                if len(str(cell.value)) > max_length:
                                    max_length = len(str(cell.value))
                            except:
                                pass
                        adjusted_width = min(max_length + 2, 50)
                        worksheet.column_dimensions[column_letter].width = adjusted_width
            
            output.seek(0)
            st.download_button(
                label="📥 Download Excel Report",
                data=output,
                file_name=f"GreenLens_AI_ROI_Analysis_{datetime.now().strftime('%Y%m%d')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            st.success("✅ Excel report generated successfully!")
        except Exception as e:
            st.error(f"❌ Error generating Excel: {str(e)}")

st.markdown("---")

# Footer
st.caption(f"""
ROI Calculator for GreenLens AI | NexusCorp Innovation Labs
Calculations based on {analysis_years}-year analysis period with {discount_rate}% discount rate
Energy price inflation: {energy_price_inflation}% annually | CO2 factor: {co2_per_kwh} kg/kWh
""")

# Additional value section
with st.expander("💡 Additional Value Beyond Direct Savings"):
    st.markdown("""
    ### Additional Business Value
    
    **1. Avoided Downtime**
    - Early detection of equipment issues prevents failures
    - Typical value: $50,000-$200,000 per prevented failure
    - Improves operational reliability and occupant comfort
    
    **2. Maintenance Optimization**
    - Predictive insights reduce unnecessary maintenance
    - Typical savings: 15-20% reduction in service calls
    - Better resource allocation for facility teams
    
    **3. Sustainability & ESG**
    - Automated CO2 tracking and reporting
    - Supports net-zero and carbon-neutral commitments
    - Enhances corporate sustainability ratings
    
    **4. Insurance Benefits**
    - Some carriers offer discounts for predictive monitoring
    - Demonstrates proactive risk management
    - Potential premium reductions: 5-10%
    
    **5. Productivity & Comfort**
    - Optimized HVAC improves occupant comfort
    - Better indoor air quality and temperature control
    - Potential productivity gains: 2-5%
    
    **Total Value of Ownership (TVO):** Often 2-3x the direct energy savings
    """)
