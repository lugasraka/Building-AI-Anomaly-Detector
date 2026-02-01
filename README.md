# GreenLens AI - Intelligent Building Anomaly Detection

An AI-powered analytics dashboard for detecting energy anomalies in commercial building HVAC systems and translating technical faults into actionable financial and sustainability metrics.

## Overview

GreenLens uses machine learning (COPOD algorithm) to identify operational inefficiencies in building energy consumption. Unlike traditional threshold-based systems that only alert when "Temp > 25°C", GreenLens detects contextual anomalies such as "high energy usage during cool weather" - indicating potential equipment faults like stuck dampers or heating valve leaks.

**Strategic Goal**: Demonstrate how predictive AI can be integrated into the EcoStruxure ecosystem to drive Energy Efficiency and Operational Performance objectives.

## Features

- **Real-time Anomaly Detection**: Uses COPOD (Copula-based Outlier Detection) algorithm for fast and accurate anomaly identification
- **Financial Impact Analysis**: Calculates wasted energy costs based on configurable energy rates
- **Sustainability Metrics**: Converts wasted energy to CO2 tonnage with configurable emission factors:
  - Grid Average: 0.4 kg/kWh
  - Renewable-Heavy: 0.2 kg/kWh
  - Coal-Heavy: 0.8 kg/kWh
  - Custom: User-defined values
- **Interactive Dashboard**: Built with Streamlit for real-time visualization and exploration
- **Explainable AI**: Shows why anomalies were flagged with temperature correlation analysis
- **Comprehensive Data**: Generates 13 realistic building variables including occupancy, HVAC status, humidity, and more
- **Model Comparison**: Jupyter notebook comparing Isolation Forest, HBOS, and COPOD algorithms
- **Program Roadmap**: Displays phased delivery plan from MVP to autonomous optimization
- **Methodology Documentation**: Detailed explanation of detection algorithms and calculations
- **About Section**: Author information and contact links

## Project Structure

```
GreenLens-AIAnomalyDetector/
├── app.py                          # Main Streamlit application
├── data_generator.py               # Synthetic building data generator (13 variables)
├── model_logic.py                  # Anomaly detection model (COPOD)
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── LICENSE                         # MIT License
├── doc/
│   └── PRD.md                     # Product Requirements Document
├── data/
│   └── building_data.csv          # Generated sensor data
└── experiments/
    ├── model_comparison.ipynb     # Algorithm comparison notebook
    ├── model_comparison_summary.csv
    └── anomaly_comparison_results.csv
```

## Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/lugasraka/Building-AI-Anomaly-Detector.git
   cd Building-AI-Anomaly-Detector
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

This creates `data/building_data.csv` with 30 days of hourly data including:
- Energy consumption (kWh)
- Outdoor and indoor temperatures
- Building occupancy
- Humidity levels
- HVAC status
- Solar irradiance
- Wind speed
- And more (13 variables total)
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
   - Select CO2 emission factor (Grid Average, Renewable-Heavy, Coal-Heavy, or Custom)
   - Regenerate simulation data with one click

2. **Business Impact Metrics**
   - Anomalies detected count
   - Estimated wasted cost (monthly)
   - Sustainability impact in tons of CO2 with selected emission factor

3. **AI Model Performance**
   - Detection rate percentage
   - Model confidence score
   - Average anomaly score

4. **Real-time Visualization**
   - Interactive Plotly chart showing energy consumption
   - Anomalies highlighted in red
   - Average baseline threshold line (orange)

5. **Governance & Explainability**
   - Model interpretability explanation
   - Common causes and recommended actions
   - Latest anomalies data table

6. **Program Roadmap**
   - Phased delivery timeline
   - Key deliverables for each phase

7. **Methodology & Calculations**
   - Anomaly detection algorithm explanation (COPOD)
   - CO2 emissions calculation formula with configurable factors
   - Cost calculation methodology

8. **About**
   - Author information and contact links

## Methodology

### Anomaly Detection

**Algorithm**: COPOD (Copula-based Outlier Detection)

**Why COPOD**:
- **Fast inference**: ~10-50ms for real-time detection
- **Better accuracy**: Handles feature correlations better than tree-based methods
- **Interpretable scores**: Direct probability-based anomaly scores
- **Production-ready**: Optimal balance of speed and accuracy for building energy monitoring

**How it works**:
1. Uses copula functions to model joint distribution between energy and temperature
2. Calculates tail probabilities - extreme tail points flagged as anomalies
3. Contamination rate set to 5% (expects 5% of data to be anomalous)
4. Features used: Energy consumption (kWh) and outdoor temperature correlation

**Why it matters**: Detects contextual anomalies that threshold-based systems miss (e.g., high energy use during cool weather indicating stuck dampers)

### CO2 Calculation

```
Formula: Wasted Energy (kWh) × Emission Factor (kg/kWh) ÷ 1000 = CO2 (Tons)

Calculation Steps:
1. Calculate average normal energy consumption
2. For each anomaly: Excess = Anomaly_Energy - Average
3. Sum all excess: Total_Wasted = Σ Excess
4. Calculate CO2 in kg: CO2_kg = Total_Wasted × Emission_Factor
5. Convert to metric tons: CO2_tons = CO2_kg ÷ 1000

Emission Factor Options (configurable in sidebar):
- Grid Average: 0.4 kg/kWh (suitable for most mixed-energy grids)
- Renewable-Heavy: 0.2 kg/kWh (high solar/wind penetration)
- Coal-Heavy: 0.8 kg/kWh (fossil fuel dominant grids)
- Custom: User-defined (0.1 - 2.0 kg/kWh range)
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

## Model Comparison

A comprehensive Jupyter notebook (`experiments/model_comparison.ipynb`) is included to compare three anomaly detection algorithms:

- **Isolation Forest**: Tree-based method (baseline)
- **HBOS**: Histogram-based Outlier Score (fastest)
- **COPOD**: Copula-based Outlier Detection (best balance)

The notebook evaluates:
- Inference speed (latency)
- Detection accuracy
- Scalability with increasing data sizes
- Feature correlation handling

To run the comparison:
```bash
cd experiments
jupyter notebook model_comparison.ipynb
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
- **ML**: PyOD (COPOD, HBOS), Scikit-Learn (Isolation Forest)
- **Frontend**: Streamlit
- **Visualization**: Plotly, Matplotlib, Seaborn
- **Data Processing**: Pandas, NumPy
- **Development**: Jupyter Notebook

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

**Raka Adrianto**  
Sustainability x AI Program Manager

- [LinkedIn](https://www.linkedin.com/in/lugasraka/)
- [GitHub](https://github.com/lugasraka)

---

**Note**: This is a prototype/PoC demonstrating AI-driven energy anomaly detection for commercial building HVAC systems.

**Version**: 2.0 - Enhanced with COPOD algorithm, configurable CO2 factors, and comprehensive model comparison
