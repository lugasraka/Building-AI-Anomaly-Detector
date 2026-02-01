# GreenLens AI - Intelligent Building Anomaly Detection

AI-powered dashboard for detecting energy anomalies in commercial building HVAC systems.

## Overview

GreenLens uses the **COPOD algorithm** to identify operational inefficiencies by detecting contextual anomalies (e.g., high energy usage during cool weather), indicating equipment faults like stuck dampers or valve leaks.

## Quick Start

```bash
# Clone and setup
git clone https://github.com/lugasraka/Building-AI-Anomaly-Detector.git
cd Building-AI-Anomaly-Detector
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Generate data and run
python data_generator.py
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

**Or use Docker:**
```bash
docker-compose up
```

## Key Features

- **COPOD Algorithm**: Fast, accurate anomaly detection optimized for building energy data
- **Financial Analysis**: Calculates wasted energy costs with configurable rates ($/kWh)
- **CO2 Tracking**: Configurable emission factors (Grid/Renewable/Coal/Custom)
- **13 Data Variables**: Energy, temperature, occupancy, HVAC status, humidity, solar, wind, etc.
- **Interactive Dashboard**: Real-time visualization with explainable AI
- **Model Comparison**: Jupyter notebook comparing Isolation Forest, HBOS, and COPOD

## Project Structure

```
├── app.py                    # Streamlit dashboard
├── model_logic.py            # COPOD anomaly detection
├── data_generator.py         # Synthetic data (13 variables)
├── requirements.txt          # Dependencies
├── data/building_data.csv    # Generated dataset
└── experiments/              # Model comparison notebook
```

## CO2 Emission Factors

| Grid Type | Factor (kg/kWh) |
|-----------|----------------|
| Grid Average | 0.4 |
| Renewable-Heavy | 0.2 |
| Coal-Heavy | 0.8 |
| Custom | User-defined |

*Configurable via sidebar in the app*

## Roadmap

| Phase | Timeline | Deliverables |
|-------|----------|--------------|
| **Phase 1** | Current | MVP with COPOD model, cost/CO2 tracking |
| **Phase 2** | Q1 2026 | Live API, feedback loop, retraining |
| **Phase 3** | Future | EcoStruxure integration, automation |

## Tech Stack

- Python 3.9+, Streamlit, Plotly
- PyOD (COPOD), Scikit-learn
- Pandas, NumPy, Jupyter
- Docker, Docker Compose

## Documentation

- [Executive Summary](EXECUTIVE_SUMMARY.md) - Business impact and stakeholder overview
- [Product Requirements Document](/doc/PRD.md) - GreenLens PRD doc

## Contact

**Raka Adrianto** - Sustainability x AI Program Manager  
[LinkedIn](https://www.linkedin.com/in/lugasraka/) | [GitHub](https://github.com/lugasraka)

---

MIT License | [LICENSE](LICENSE)
