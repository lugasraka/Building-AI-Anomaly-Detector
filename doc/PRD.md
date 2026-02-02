# Product Requirement Document (PRD)

**Project Name:** GreenLens: AI-Driven Energy Anomaly Detection
**Version:** 1.0 (MVP)
**Status:** Prototype / PoC
**Author:** [Your Name]
**Date:** January 2026

---

## 1. Executive Summary

GreenLens is an AI-enabled analytics module designed to identify operational inefficiencies in commercial building HVAC systems. By analyzing historical sensor data and detecting anomalies in real-time, GreenLens translates technical faults into actionable financial and sustainability metrics.
**Strategic Goal:** To demonstrate how predictive AI can be integrated into the **IntelliCore** ecosystem to drive the "Energy Efficiency" and "Operational Performance" objectives of Smart Energy Division.

---

## 2. Problem Statement

Commercial buildings often suffer from "energy drift"—gradual inefficiencies in HVAC performance that go unnoticed by rule-based building management systems (BMS).

* **The Pain Point:** Facility managers react to equipment failures rather than predicting them.
* **The Cost:** Unnecessary energy consumption (increasing OpEx) and higher carbon footprint (impacting sustainability goals).
* **The Gap:** Current solutions alert on *thresholds* (e.g., "Temp > 25°C") but miss *contextual anomalies* (e.g., "Power usage is high despite cool weather").

---

## 3. Strategic Alignment (The "Why")

This initiative supports the Smart Energy Division by:

1. **Enhancing Operational Efficiency:** Reducing "Time to Detect" (TTD) for equipment faults.
2. **Sustainability:** Directly correlating energy spikes to CO2 tonnage.
3. **Vision Integration:** Designed as a micro-service that could feed into the **IntelliCore Vision** platform roadmap.

---

## 4. User Personas

| Persona | Role | Key Question |
| --- | --- | --- |
| **Alex, the Facility Manager** | Operational User | "Where is my building wasting energy *right now*, and what is the specific cause?" |
| **Sarah, the Sustainability Lead** | Business Stakeholder | "How much CO2 did we save this month by fixing these anomalies?" |

---

## 5. Functional Requirements (Scope)

### 5.1 The "GreenLens" Dashboard

* **FR-01:** Display a real-time time-series chart of Power Consumption (kW) vs. External Temperature.
* **FR-02:** Highlight anomalous data points in **Red** where the AI model predicts deviation from normal behavior.
* **FR-03:** Calculate and display "Estimated Wasted Cost" based on the area under the anomaly curve.

### 5.2 AI Engine & Analytics

* **FR-04:** Deploy an unsupervised learning model (Isolation Forest or Autoencoder) trained on standard ASHRAE building data.
* **FR-05:** **Explainability:** When an anomaly is clicked, show the *top contributing features* (e.g., "Fan Speed was high while Occupancy was zero").

### 5.3 Technical Governance

* **FR-06:** Model Performance Monitor: Display current model accuracy/health to ensure reliability.

---

## 6. Technical Architecture & Constraints

* **Deployment Strategy:**
* *MVP:* Local/Cloud Web App (Streamlit).
* *Production Vision:* Hybrid Architecture. Inference runs at the **Edge** (on-premise BMS) for low latency; Model training runs in **Cloud** (AWS/Azure) for scalability.


* **Data Privacy:** All PII (Personally Identifiable Information) regarding building occupancy must be anonymized before ingestion, adhering to GDPR standards.
* **Tech Stack:**
* **Core:** Python 3.9
* **ML:** Scikit-Learn (Isolation Forest), SHAP (Explainability).
* **Frontend:** Streamlit.
* **Containerization:** Docker (to demonstrate deployment readiness).



---

## 7. Roadmap (Phased Delivery)

This roadmap simulates a Program Manager's view of scaling the solution.

* **Phase 1: MVP (Current Scope)**
* Ingest static historical data (CSV).
* Train baseline anomaly detection model.
* Visualize cost impact.
* *Goal: Proof of Value.*


* **Phase 2: Connectivity & Feedback (Q1 2026)**
* Connect to live API stream.
* Implement "User Feedback Loop" (User marks anomaly as True/False) to retrain model.
* *Goal: Operational Integration.*


* **Phase 3: Automated Control (Future)**
* Integration with IntelliCore Building Management for automated setpoint adjustment based on predictions.
* *Goal: Autonomous Energy Optimization.*



---

## 8. Success Metrics (KPIs)

To judge the success of this program, we track:

| Category | Metric | Target |
| --- | --- | --- |
| **Business Value** | Potential Energy Cost Identified | > $10,000 / year simulated |
| **Operational** | Reduction in Mean Time to Detect (MTTD) | -30% vs Rule-Based Systems |
| **AI Performance** | Precision (True Positives / Total Flags) | > 85% (Minimize alert fatigue) |

---

## 9. Risks & Mitigation

* **Risk:** Alert Fatigue (Model flagging too many false positives).
* *Mitigation:* Implementation of a "sensitivity slider" for the Facility Manager to adjust threshold.


* **Risk:** Data Drift (Building usage patterns change).
* *Mitigation:* Scheduled monthly model retraining pipeline.