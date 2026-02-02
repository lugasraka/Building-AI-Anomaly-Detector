# AI Solutions Portfolio - Project Charters
## Detailed Project Definitions, Scope & Success Criteria

**Document Version:** 1.0  
**Last Updated:** February 2026  
**Classification:** Internal Use - Strategic Planning

---

## Project 1: GreenLens AI - Intelligent Building Anomaly Detection

### Executive Summary

**Status:** Active (Phase 2: Scale)  
**Timeline:** Q1 2026 - Q2 2026 (Phase 2)  
**Investment:** $150,000  
**Expected ROI:** 180% over 3 years  
**Project Lead:** Raka Adrianto (Program Manager)

### Problem Statement

Commercial buildings waste 15-30% of energy due to undetected HVAC inefficiencies. Traditional monitoring systems use simple thresholds that generate 80% false positives, causing alert fatigue and missed opportunities. Facility managers need intelligent systems that detect contextual anomalies and provide actionable insights.

### Solution Overview

GreenLens AI uses the COPOD (Copula-based Outlier Detection) algorithm to identify contextual anomalies in building energy consumption. Unlike threshold-based systems, it correlates multiple variables (energy, temperature, occupancy, weather) to detect issues like "high energy use during cool weather" indicating stuck dampers.

**Key Capabilities:**
- Real-time anomaly detection (<50ms inference)
- Root cause analysis (HVAC, schedule, equipment issues)
- Automatic ROI calculation ($ cost and CO2 impact)
- Integration with IntelliCore Building Management

### Scope & Deliverables

**Phase 1: MVP (Complete)**
- ✅ COPOD anomaly detection model
- ✅ Streamlit dashboard for visualization
- ✅ Business impact metrics (cost, CO2)
- ✅ Docker containerization
- ✅ Synthetic data for testing

**Phase 2: Scale (Current - Q1-Q2 2026)**
- [ ] Deploy to 12 buildings (currently: 10)
- [ ] IntelliCore API integration
- [ ] Production MLOps pipeline
- [ ] Customer success program
- [ ] Automated reporting

**Phase 3: Optimize (Future - Q3 2026+)**
- [ ] Automated control recommendations
- [ ] Predictive maintenance integration
- [ ] Multi-building portfolio analytics
- [ ] Advanced root cause analysis

### Success Criteria

**Technical Metrics:**
- Anomaly detection latency: <50ms (p95)
- Model confidence: >96%
- False positive rate: <15%
- System uptime: 99.9%

**Business Metrics:**
- Energy savings: 15-20% per building
- Cost avoidance: $2,000-$10,000 per building annually
- CO2 reduction: 400-800 tons per building annually
- Customer satisfaction (NPS): >50

**Adoption Metrics:**
- Buildings deployed: 12 by Q2 2026
- Active users: 50+ facility managers
- Monthly active usage: >80% of deployed buildings

### Resource Requirements

**Team Allocation:**
- AI Engineer I: 50% (model improvements)
- AI Engineer II: 30% (architecture, integration)
- MLOps Engineer: 40% (production pipeline)
- Data Scientist: 20% (validation, reporting)

**Budget Breakdown:**
- Personnel: $108,000 (72%)
- Infrastructure: $18,000 (12%)
- Tools & Software: $7,500 (5%)
- Training: $9,000 (6%)
- Contingency: $7,500 (5%)

### Risks & Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Integration complexity | Medium | High | Early API testing, dedicated integration engineer |
| Customer adoption | Low | High | Pilot success stories, outcome-based pricing |
| Model accuracy in production | Medium | Medium | Continuous monitoring, feedback loops, retraining |
| Data quality issues | Medium | Medium | Data validation pipeline, quality alerts |

### Dependencies

**Internal:**
- IntelliCore Building Management team (API access)
- Customer Success team (deployment support)
- Sales team (customer acquisition)

**External:**
- Customer BMS systems (data access)
- Cloud infrastructure (AWS/Azure)
- Third-party weather APIs

### Project Status (Current)

**Health:** 🟢 On Track

**Recent Achievements:**
- Deployed to 10 buildings (target: 12)
- Validated $400K annual savings
- Achieved 99.95% uptime
- MLOps monitoring dashboard live

**Current Focus:**
- Complete IntelliCore integration
- Deploy to final 2 buildings
- Launch customer success program

**Blockers:**
- None currently

---

## Project 2: Predictive HVAC Maintenance

### Executive Summary

**Status:** Planning (Phase 1)  
**Timeline:** Q2 2026 - Q4 2026  
**Investment:** $200,000  
**Expected ROI:** 220% over 3 years  
**Project Lead:** TBD (AI Engineer II)

### Problem Statement

HVAC equipment failures in commercial buildings result in:
- Unplanned downtime costing $50K-$200K per incident
- Emergency repair premiums (2-3x normal cost)
- Occupant comfort complaints and productivity loss
- Equipment lifespan reduction due to reactive maintenance

Current preventive maintenance is time-based (every 3 months), not condition-based, leading to unnecessary service calls or missed early warning signs.

### Solution Overview

Predictive HVAC Maintenance uses machine learning to:
- Predict equipment failures 2-4 weeks in advance
- Identify optimal maintenance timing (condition-based)
- Prioritize work orders by criticality and cost impact
- Extend equipment lifespan through proactive care

**ML Approach:**
- Time-series forecasting (LSTM, Prophet) for degradation patterns
- Anomaly detection for early warning signals
- Survival analysis for remaining useful life (RUL) estimation
- Multi-variate analysis (vibration, temperature, power draw)

### Scope & Deliverables

**Phase 1: MVP (Q2-Q3 2026)**
- [ ] Data pipeline for HVAC sensor data
- [ ] Failure prediction models (3 equipment types)
- [ ] Maintenance scheduling algorithm
- [ ] Technician mobile app
- [ ] Integration with CMMS (ServiceNow)
- [ ] Pilot deployment (2 buildings)

**Phase 2: Scale (Q4 2026 - Q1 2027)**
- [ ] Expand to 10+ buildings
- [ ] Additional equipment types (chillers, boilers, AHUs)
- [ ] Automated work order generation
- [ ] ROI validation and reporting
- [ ] Integration with GreenLens AI

**Phase 3: Optimize (Q2 2027+)**
- [ ] Prescriptive maintenance (what to fix, not just when)
- [ ] Parts inventory optimization
- [ ] Vendor performance tracking
- [ ] Industry benchmarking

### Success Criteria

**Technical Metrics:**
- Prediction accuracy: 85%+ (2-week horizon)
- False positive rate: <20%
- Lead time: 10-14 days average
- Model refresh: Monthly with new data

**Business Metrics:**
- Equipment uptime improvement: +25%
- Maintenance cost reduction: 20-30%
- Emergency repairs avoided: 70%+
- Equipment lifespan extension: 15-20%

**Operational Metrics:**
- Technician efficiency: +30% (right fix, right time)
- Parts inventory optimization: 15% reduction
- Customer satisfaction: >4.5/5.0

### Resource Requirements

**Team Allocation:**
- AI Engineer II: 60% (lead, model development)
- AI Engineer I: 80% (feature engineering, data pipeline)
- MLOps Engineer: 30% (deployment, monitoring)
- Data Scientist: 30% (validation, feature analysis)

**Budget Breakdown:**
- Personnel: $144,000 (72%)
- Infrastructure: $24,000 (12%)
- CMMS Integration: $10,000 (5%)
- Training: $12,000 (6%)
- Contingency: $10,000 (5%)

### Risks & Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Data availability | Medium | High | Early data assessment, synthetic data fallback |
| Integration with legacy CMMS | Medium | Medium | API-first design, middleware if needed |
| Technician adoption | Medium | Medium | Mobile-first UX, training program, incentives |
| Model accuracy | Medium | High | Conservative thresholds, human-in-the-loop |

### Dependencies

**Internal:**
- GreenLens AI (data foundation)
- Customer Success (pilot coordination)
- Product team (requirements)

**External:**
- CMMS vendors (ServiceNow, IBM Maximo)
- HVAC OEMs (equipment data protocols)
- Customer facilities (sensor installation)

### Business Case

**Investment:** $200K over 9 months  
**Expected Returns:**
- Year 1: $150K (pilot buildings)
- Year 2: $600K (scaled deployment)
- Year 3: $800K (optimization)
- **3-Year NPV:** $440K  
- **ROI:** 220%  
- **Payback:** 11 months

---

## Project 3: Energy Demand Forecasting

### Executive Summary

**Status:** Planning (Ideation)  
**Timeline:** Q3 2026 - Q1 2027  
**Investment:** $180,000  
**Expected ROI:** 150% over 3 years  
**Project Lead:** TBD (Data Scientist)

### Problem Statement

Building operators struggle with:
- Peak demand charges (30-50% of electricity bill)
- Suboptimal HVAC scheduling (running when not needed)
- Inability to participate in demand response programs
- Lack of visibility into 24-hour ahead consumption

Current forecasting relies on simple rules or historical averages, missing weather impacts, occupancy patterns, and equipment schedules.

### Solution Overview

Energy Demand Forecasting provides:
- 24-hour ahead energy consumption predictions (hourly granularity)
- Peak demand alerts with recommended actions
- Optimal HVAC scheduling recommendations
- Demand response program participation support

**ML Approach:**
- Time-series forecasting (ARIMA, Prophet, LSTM)
- Weather feature engineering (temperature, humidity, solar)
- Calendar features (holidays, events, schedules)
- Ensemble methods for robust predictions

### Scope & Deliverables

**Phase 1: MVP (Q3-Q4 2026)**
- [ ] 24-hour forecasting model (1-hour granularity)
- [ ] Weather data integration
- [ ] Peak demand alerting system
- [ ] Dashboard for operators
- [ ] API for BMS integration
- [ ] Pilot deployment (3 buildings)

**Phase 2: Scale (Q1-Q2 2027)**
- [ ] Expand to 15+ buildings
- [ ] 7-day ahead forecasting
- [ ] Automated HVAC scheduling recommendations
- [ ] Demand response integration
- [ ] Cost optimization algorithms

**Phase 3: Optimize (Q3 2027+)**
- [ ] Real-time pricing optimization
- [ ] Battery storage integration
- [ ] Renewable energy forecasting
- [ ] Grid services participation

### Success Criteria

**Technical Metrics:**
- Forecast accuracy (MAPE): <10% (24-hour)
- Forecast accuracy (MAPE): <15% (7-day)
- Prediction latency: <5 seconds
- Model update frequency: Daily

**Business Metrics:**
- Peak demand reduction: 15-20%
- Energy cost savings: 10-15%
- Demand response revenue: $5K-$20K per building annually
- Payback period: <12 months

**Operational Metrics:**
- Alert accuracy: >90%
- User engagement: >70% daily active
- Schedule optimization adoption: >60%

### Resource Requirements

**Team Allocation:**
- Data Scientist: 70% (lead, forecasting models)
- AI Engineer I: 60% (feature engineering, API)
- AI Engineer II: 20% (architecture review)
- MLOps Engineer: 20% (deployment)

**Budget Breakdown:**
- Personnel: $129,600 (72%)
- Infrastructure: $21,600 (12%)
- Weather API: $9,000 (5%)
- Training: $10,800 (6%)
- Contingency: $9,000 (5%)

### Risks & Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Weather data quality | Medium | High | Multiple sources, backup providers |
| Model accuracy in extreme weather | Medium | Medium | Ensemble methods, confidence intervals |
| BMS integration complexity | Medium | Medium | Standard APIs, phased rollout |
| Operator adoption | Medium | Medium | Training, intuitive UI, clear value |

### Dependencies

**Internal:**
- GreenLens AI (historical data)
- Predictive Maintenance (equipment status)
- Product team (UX design)

**External:**
- Weather data providers (OpenWeather, Dark Sky)
- Utility companies (demand response programs)
- BMS vendors (scheduling API access)

### Business Case

**Investment:** $180K over 6 months  
**Expected Returns:**
- Year 1: $100K (pilot + initial scale)
- Year 2: $400K (full deployment)
- Year 3: $500K (optimization)
- **3-Year NPV:** $270K  
- **ROI:** 150%  
- **Payback:** 13 months

---

## Project 4: Smart Occupancy Optimization

### Executive Summary

**Status:** Ideation  
**Timeline:** Q4 2026 - Q2 2027  
**Investment:** $120,000  
**Expected ROI:** 140% over 3 years  
**Project Lead:** TBD (AI Engineer I)

### Problem Statement

Commercial buildings often run HVAC systems based on:
- Fixed schedules (8 AM - 6 PM) regardless of actual occupancy
- Worst-case assumptions (full occupancy every day)
- No real-time adjustment based on actual usage

This results in:
- 20-30% energy waste in over-conditioned spaces
- Comfort complaints in under-conditioned areas
- Inability to support flexible/hybrid work patterns

### Solution Overview

Smart Occupancy Optimization uses AI to:
- Detect real-time occupancy (WiFi, sensors, badging data)
- Predict occupancy patterns (meeting schedules, historical trends)
- Optimize HVAC zones dynamically based on actual usage
- Support flexible work and hot-desking models

**ML Approach:**
- Occupancy detection (computer vision, sensor fusion)
- Pattern recognition (clustering, time-series)
- Predictive modeling (schedule + historical + real-time)
- Optimization algorithms (zone control, setpoint adjustment)

### Scope & Deliverables

**Phase 1: MVP (Q4 2026 - Q1 2027)**
- [ ] Occupancy detection system (WiFi + sensors)
- [ ] Real-time occupancy dashboard
- [ ] HVAC zone optimization algorithm
- [ ] Integration with BMS for control
- [ ] Pilot deployment (2 buildings)

**Phase 2: Scale (Q2-Q3 2027)**
- [ ] Expand to 8+ buildings
- [ ] Predictive occupancy (24-hour ahead)
- [ ] Hot-desking support features
- [ ] Space utilization analytics
- [ ] Integration with calendaring systems

**Phase 3: Optimize (Q4 2027+)**
- [ ] Multi-floor optimization
- [ ] Air quality balancing (CO2, VOCs)
- [ ] Personalized comfort profiles
- [ ] Post-COVID hybrid work optimization

### Success Criteria

**Technical Metrics:**
- Occupancy detection accuracy: >95%
- HVAC efficiency improvement: +20%
- Response time: <2 minutes (zone adjustment)
- System availability: 99.5%

**Business Metrics:**
- Energy savings: 15-25% in optimized zones
- Cost savings: $3K-$8K per building annually
- Comfort complaints: -40%
- Space utilization: +15% efficiency

**User Experience Metrics:**
- Occupant satisfaction: >4.0/5.0
- Hot-desking adoption: >50% (if applicable)
- Facility manager satisfaction: >4.5/5.0

### Resource Requirements

**Team Allocation:**
- AI Engineer I: 70% (lead, optimization algorithms)
- AI Engineer II: 30% (architecture, integration)
- MLOps Engineer: 20% (deployment)
- Data Scientist: 20% (pattern analysis)

**Budget Breakdown:**
- Personnel: $86,400 (72%)
- Infrastructure: $14,400 (12%)
- Sensors & Hardware: $6,000 (5%)
- Training: $7,200 (6%)
- Contingency: $6,000 (5%)

### Risks & Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Privacy concerns | Medium | High | Anonymous detection, opt-in, GDPR compliance |
| Sensor installation cost | Medium | Medium | Use existing infrastructure (WiFi), phased rollout |
| BMS control limitations | Medium | High | API assessment, fallback to recommendations only |
| Occupant resistance | Low | Medium | Change management, comfort guarantees |

### Dependencies

**Internal:**
- GreenLens AI (energy baseline)
- Demand Forecasting (load prediction)
- IT team (WiFi data access)

**External:**
- Sensor vendors (if new hardware needed)
- BMS vendors (zone control APIs)
- Privacy/legal (data handling compliance)

### Business Case

**Investment:** $120K over 6 months  
**Expected Returns:**
- Year 1: $60K (pilot buildings)
- Year 2: $300K (scaled deployment)
- Year 3: $400K (optimization)
- **3-Year NPV:** $168K  
- **ROI:** 140%  
- **Payback:** 14 months

---

## Cross-Project Synergies

### Data Sharing

**GreenLens AI → All Projects:**
- Historical energy consumption patterns
- Anomaly detection baseline
- Building characterization data

**Predictive Maintenance ↔ Demand Forecasting:**
- Equipment health impacts on energy demand
- Maintenance schedules affect forecasting accuracy

**All Projects → Occupancy Optimization:**
- Occupancy patterns inform anomaly detection
- Equipment status affects zone optimization
- Demand forecasts inform occupancy predictions

### Platform Synergies

**Shared Infrastructure:**
- MLOps platform (model registry, monitoring)
- Data pipeline and feature store
- Cloud infrastructure (cost optimization)
- Security and compliance framework

**Reusable Components:**
- Time-series preprocessing library
- Anomaly detection algorithms
- Visualization dashboard framework
- API integration patterns

### Business Synergies

**Customer Value Proposition:**
- **Individual Projects:** 10-20% savings each
- **Combined Portfolio:** 25-35% total savings
- **Integrated Platform:** 40%+ with optimization

**Sales Strategy:**
- Land with GreenLens AI (easiest adoption)
- Expand with Predictive Maintenance (high value)
- Optimize with Demand + Occupancy (advanced)

---

## Portfolio Investment Summary

| Project | Investment | Timeline | ROI | Priority |
|---------|------------|----------|-----|----------|
| **GreenLens AI** | $150K | Q1-Q2 2026 | 180% | P1 - Active |
| **Predictive Maintenance** | $200K | Q2-Q4 2026 | 220% | P1 - High |
| **Demand Forecasting** | $180K | Q3 26-Q1 27 | 150% | P2 - Medium |
| **Occupancy Optimization** | $120K | Q4 26-Q2 27 | 140% | P2 - Medium |
| **TOTAL** | **$650K** | **18 months** | **165%** | - |

**Priority Rationale:**
- **P1 (High):** Foundation + High ROI
- **P2 (Medium):** Optimization + Strategic value

---

## Document Control

**Owner:** Raka Adrianto, AI Solution Program Manager  
**Review Cycle:** Monthly (sprint reviews) + Quarterly (portfolio review)  
**Next Review:** March 2026 (Q1 Portfolio Review)  
**Distribution:** Steering Committee, Project Leads, AI Team  
**Classification:** Internal Use - Strategic Planning

---

*These project charters define the scope, success criteria, and resource requirements for each AI initiative. For detailed operational plans, refer to individual project backlogs and sprint documentation.*
