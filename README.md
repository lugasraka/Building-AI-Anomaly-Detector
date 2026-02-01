# GreenLens AI - Intelligent Building Anomaly Detection

An AI-powered analytics dashboard for detecting energy anomalies in commercial building HVAC systems and translating technical faults into actionable financial and sustainability metrics.

## Overview

GreenLens uses machine learning (Isolation Forest algorithm) to identify operational inefficiencies in building energy consumption. Unlike traditional threshold-based systems that only alert when "Temp > 25°C", GreenLens detects contextual anomalies such as "high energy usage during cool weather" - indicating potential equipment faults like stuck dampers or heating valve leaks.

**Strategic Goal**: Demonstrate how predictive AI can be integrated into the EcoStruxure ecosystem to drive Energy Efficiency and Operational Performance objectives.

## Features

- **Real-time Anomaly Detection**: Uses Isolation Forest algorithm to identify energy consumption anomalies
- **Financial Impact Analysis**: Calculates wasted energy costs based on configurable energy rates
- **Sustainability Metrics**: Converts wasted energy to CO2 tonnage (0.0004 tons per kWh)
- **Interactive Dashboard**: Built with Streamlit for real-time visualization and exploration
- **Explainable AI**: Shows why anomalies were flagged with temperature correlation analysis
- **Program Roadmap**: Displays phased delivery plan from MVP to autonomous optimization
- **Methodology Documentation**: Detailed explanation of detection algorithms and calculations

## Project Structure

```
GreenLens-AIAnomalyDetector/
├── app.py                 # Main Streamlit application
├── data_generator.py      # Synthetic building data generator
├── model_logic.py         # Anomaly detection model (Isolation Forest)
├── requirements.txt       # Python dependencies
├── doc/
│   └── PRD.md            # Product Requirements Document
└── data/
    └── building_data.csv  # Generated sensor data
```

## Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd GreenLens-AIAnomalyDetector
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Generate Sample Data

First, generate the synthetic building data:

```bash
python data_generator.py
```

This creates `data/building_data.csv` with 30 days of hourly energy consumption data including:
- Daily usage cycles (higher during 8am-6pm)
- Weekend reduction (60% lower usage)
- Random sensor noise
- 15 injected anomalies (energy spikes)

### Run the Dashboard

Start the Streamlit application:

```bash
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501`

### Dashboard Features

1. **Configuration Sidebar**
   - Adjust energy cost per kWh (default: $0.15)
   - Regenerate simulation data with one click

2. **Business Impact Metrics**
   - Anomalies detected count
   - Estimated wasted cost (monthly)
   - Sustainability impact in tons of CO2

3. **Real-time Visualization**
   - Interactive Plotly chart showing energy consumption
   - Anomalies highlighted in red
   - Average baseline threshold line

4. **Governance & Explainability**
   - Model interpretability explanation
   - Detailed anomaly data table

5. **Program Roadmap**
   - Phased delivery timeline
   - Key deliverables for each phase

6. **Methodology & Calculations**
   - Anomaly detection algorithm explanation
   - CO2 emissions calculation formula
   - Cost calculation methodology

## Methodology

### Anomaly Detection

**Algorithm**: Isolation Forest (unsupervised learning)

**How it works**:
1. Randomly selects features and split values to isolate data points
2. Anomalies require fewer splits to isolate (shorter path length)
3. Contamination rate set to 5% (expects 5% of data to be anomalous)
4. Features used: Energy consumption (kWh) and outdoor temperature

**Why it matters**: Detects contextual anomalies that threshold-based systems miss

### CO2 Calculation

```
Formula: Wasted Energy (kWh) × 0.0004 = CO2 Tons

Calculation Steps:
1. Calculate average normal energy consumption
2. For each anomaly: Excess = Anomaly_Energy - Average
3. Sum all excess: Total_Wasted = Σ Excess
4. Convert to CO2: CO2 = Total_Wasted × 0.0004

Emission Factor: 0.0004 tons CO2 per kWh
```

### Cost Calculation

```
Formula: Wasted Energy (kWh) × Cost per kWh = Wasted Cost ($)

Calculation Steps:
1. Calculate average normal energy consumption
2. For each anomaly: Excess = Anomaly_Energy - Average
3. Sum all excess energy: Total_Wasted_kWh = Σ Excess
4. Apply cost rate: Cost = Total_Wasted_kWh × Cost_per_kWh

Current Rate: $0.15 per kWh (configurable in sidebar)
```

## Roadmap

| Phase | Timeline | Key Deliverables | Goal |
|-------|----------|------------------|------|
| **Phase 1: MVP** | Current | CSV data ingestion, Baseline model, Cost visualization | Proof of Value |
| **Phase 2: Connectivity** | Q1 2026 | Live API stream, User feedback loop, Model retraining | Operational Integration |
| **Phase 3: Automation** | Future | EcoStruxure integration, Automated setpoint control | Autonomous Optimization |

## Success Metrics (KPIs)

| Category | Metric | Target |
|----------|--------|--------|
| **Business Value** | Potential Energy Cost Identified | > $10,000/year simulated |
| **Operational** | Reduction in Mean Time to Detect (MTTD) | -30% vs Rule-Based Systems |
| **AI Performance** | Precision (True Positives / Total Flags) | > 85% |

## Tech Stack

- **Core**: Python 3.9+
- **ML**: Scikit-Learn (Isolation Forest)
- **Frontend**: Streamlit
- **Visualization**: Plotly
- **Data Processing**: Pandas, NumPy

## User Personas

| Persona | Role | Key Question |
|---------|------|--------------|
| **Alex, Facility Manager** | Operational User | "Where is my building wasting energy right now, and what is the specific cause?" |
| **Sarah, Sustainability Lead** | Business Stakeholder | "How much CO2 did we save this month by fixing these anomalies?" |

## Data Privacy

All PII (Personally Identifiable Information) regarding building occupancy is anonymized before ingestion, adhering to GDPR standards.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

Raka Adrianto, Sustainability x AI Program manager [Linkedin](https://www.linkedin.com/in/lugasraka/)

---

**Note**: This is a prototype/PoC demonstrating AI-driven energy anomaly detection for commercial building HVAC systems.