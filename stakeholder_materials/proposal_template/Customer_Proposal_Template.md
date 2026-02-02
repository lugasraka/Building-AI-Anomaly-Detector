# GreenLens AI - Customer Proposal Template
## AI-Powered Building Energy Optimization

**Proposal Date:** [DATE]  
**Proposal Version:** [VERSION]  
**Valid Until:** [DATE + 90 days]  

**Prepared for:**  
[CLIENT COMPANY NAME]  
[CLIENT ADDRESS]  

**Prepared by:**  
Raka Adrianto  
Sustainability x AI Program Manager  
NexusCorp Innovation Labs  
raka.adrianto@nexuscorp.com | +65 XXXX XXXX

---

## 1. EXECUTIVE SUMMARY

### Opportunity Overview

[CLIENT COMPANY NAME] has the opportunity to reduce energy consumption by **15-20%** across their building portfolio through AI-powered anomaly detection. GreenLens AI identifies operational inefficiencies in real-time, translating technical issues into actionable financial and sustainability metrics.

### Proposed Solution

NexusCorp proposes implementing **GreenLens AI**, an intelligent anomaly detection system that:
- Monitors building energy consumption patterns using advanced AI (COPOD algorithm)
- Detects contextual anomalies (e.g., high energy use during cool weather indicating stuck dampers)
- Translates anomalies into financial impact ($ cost) and sustainability metrics (CO2 reduction)
- Provides root cause analysis and actionable recommendations

### Expected Outcomes

| Metric | Conservative | Target | Optimistic |
|--------|--------------|--------|------------|
| **Energy Savings** | 12% | 18% | 25% |
| **Annual Cost Avoidance** | $[XXX,XXX] | $[XXX,XXX] | $[XXX,XXX] |
| **CO2 Reduction** | [XXX] tons | [XXX] tons | [XXX] tons |
| **Payback Period** | 18 months | 12 months | 8 months |
| **3-Year ROI** | 120% | 180% | 250% |

### Investment Summary

**Total Project Investment:** $[XXX,XXX]  
**Annual Subscription:** $[XX,XXX]  
**Implementation Timeline:** [X] months  
**Recommended Approach:** Phased rollout starting with pilot deployment

---

## 2. CLIENT CONTEXT & OBJECTIVES

### Current Situation

[CLIENT COMPANY NAME] operates **[NUMBER] buildings** totaling **[SQUARE FOOTAGE]** across **[LOCATIONS]**. Current energy management challenges include:

- **Annual Energy Spend:** $[XXX,XXX]
- **Primary Energy Systems:** [HVAC / Lighting / Equipment / etc.]
- **Current Monitoring:** [BMS / Manual / Basic Analytics / None]
- **Key Pain Points:**
  - [Pain point 1: e.g., Undetected HVAC inefficiencies]
  - [Pain point 2: e.g., Lack of visibility into energy waste]
  - [Pain point 3: e.g., Reactive maintenance approach]
  - [Pain point 4: e.g., Sustainability reporting challenges]

### Strategic Objectives

Based on our discovery workshop, [CLIENT COMPANY NAME] has identified the following strategic objectives:

1. **Operational Efficiency**
   - Reduce energy waste by [X]% within [Y] years
   - Improve Mean Time to Detect (MTTD) for equipment issues
   - Optimize HVAC operations and maintenance schedules

2. **Financial Performance**
   - Achieve $[XXX,XXX] annual cost savings
   - Reduce maintenance costs through predictive insights
   - Improve budget predictability

3. **Sustainability Goals**
   - Reduce CO2 emissions by [X] tons annually
   - Support [ESG / Net Zero / Carbon Neutral] commitments
   - Enhance sustainability reporting capabilities

4. **Technology Modernization**
   - Leverage AI/ML for building optimization
   - Integrate with existing [IntelliCore / BMS / IoT] infrastructure
   - Enable data-driven decision making

### Success Criteria

This project will be considered successful when:
- [Criterion 1: e.g., 15% energy reduction demonstrated within 6 months]
- [Criterion 2: e.g., $XXX,XXX cost savings validated]
- [Criterion 3: e.g., Automated monthly sustainability reports generated]
- [Criterion 4: e.g., Facility team trained and self-sufficient]

---

## 3. PROPOSED SOLUTION

### Solution Overview

GreenLens AI is an intelligent anomaly detection system that uses advanced machine learning to identify energy inefficiencies in commercial buildings. Unlike traditional threshold-based systems, GreenLens AI detects **contextual anomalies** by analyzing correlations between multiple variables.

**Example:**
- **Traditional System:** "Alert if energy > 500 kWh" (80% false positives)
- **GreenLens AI:** "High energy + cool weather = Damper issue" (15% false positives)

### Technical Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    GreenLens AI Platform                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │  Data Layer  │ →  │  AI Engine   │ →  │   Business   │  │
│  │              │    │              │    │ Intelligence │  │
│  │ • IntelliCore│    │ • COPOD      │    │ • Cost       │  │
│  │ • BMS API    │    │   Algorithm  │    │   Analysis   │  │
│  │ • IoT Sensors│    │ • Real-time  │    │ • CO2        │  │
│  │ • CSV/JSON   │    │   Inference  │    │   Tracking   │  │
│  └──────────────┘    └──────────────┘    └──────────────┘  │
│         ↓                   ↓                   ↓           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Actionable Insights                      │  │
│  │  • Anomaly Alerts    • Root Cause Analysis           │  │
│  │  • HVAC Schedules    • Maintenance Recommendations   │  │
│  │  • Setpoint Controls • Sustainability Reports        │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Key Capabilities

**1. Real-Time Anomaly Detection**
- **Algorithm:** COPOD (Copula-based Outlier Detection)
- **Performance:** <50ms inference latency, 96% confidence
- **Features:** Monitors 13 variables (energy, temperature, occupancy, HVAC status, etc.)
- **Learning:** Unsupervised - no labeled training data required

**2. Business Impact Translation**
- Automatic cost calculation based on energy rates
- CO2 emission tracking with configurable factors
- ROI dashboard for executive reporting
- Monthly savings validation reports

**3. Root Cause Analysis**
- Identifies HVAC issues (stuck dampers, faulty sensors)
- Detects schedule problems (weekend operations, after-hours usage)
- Flags equipment faults (leaks, actuator failures)
- Provides actionable recommendations

**4. Integration & Deployment**
- **IntelliCore Native:** Pre-built connectors for IntelliCore Building Management
- **Flexible Deployment:** Cloud, Edge, or Hybrid architectures
- **API-First:** REST APIs for custom integrations
- **Secure:** SOC 2 Type II, GDPR compliant

### Scope of Work

**Phase 1: Pilot Deployment (Months 1-3)**

*Included in Base Price:*
- [ ] Deploy GreenLens AI in [NUMBER] pilot buildings
- [ ] Integrate with existing [BMS / IntelliCore / Data sources]
- [ ] Historical data analysis and baseline establishment
- [ ] Model training and calibration for building profile
- [ ] Real-time anomaly detection activation
- [ ] Dashboard configuration and customization
- [ ] User training for facility management team (2 sessions)
- [ ] Technical documentation and runbooks
- [ ] Weekly progress reports during deployment
- [ ] Monthly performance reports (3 months)

*Deliverables:*
- Validated energy savings measurement
- Calibrated AI model for your building characteristics
- Trained facility team (up to 10 users)
- Technical integration documentation
- Pilot success report with ROI validation

**Phase 2: Scale & Optimize (Months 4-9)**

*Included in Annual Subscription:*
- [ ] Rollout to remaining [NUMBER] buildings
- [ ] Advanced analytics and cross-building pattern analysis
- [ ] Automated alerting workflows (email/SMS/dashboard)
- [ ] Executive dashboard for portfolio visibility
- [ ] Quarterly business reviews and optimization
- [ ] Model updates and continuous improvement
- [ ] 24/7 technical support
- [ ] Quarterly training refreshers

*Optional Add-Ons:*
- [ ] Predictive maintenance integration (+$XX,XXX)
- [ ] Automated control implementation (+$XX,XXX)
- [ ] Custom reporting and analytics (+$XX,XXX)
- [ ] Advanced MLOps monitoring (+$XX,XXX)

---

## 4. IMPLEMENTATION ROADMAP

### Project Timeline

| Phase | Duration | Key Activities | Deliverables |
|-------|----------|----------------|--------------|
| **Week 1-2** | Discovery | Requirements gathering, system audit, data assessment | Technical architecture document |
| **Week 3-4** | Design | Solution design, integration planning, security review | Implementation plan |
| **Month 2** | Pilot Deploy | Install, configure, integrate, train model | Pilot system live |
| **Month 3** | Validation | Baseline measurement, accuracy validation, user training | Pilot success report |
| **Month 4-6** | Scale | Rollout to additional buildings, advanced features | Portfolio deployment |
| **Month 7-9** | Optimize | Performance tuning, advanced analytics, automation | Optimized system |
| **Ongoing** | Support | 24/7 support, model updates, quarterly reviews | Continuous improvement |

### Resource Requirements

**NexusCorp Team:**
- AI Solution Program Manager (Raka Adrianto) - Overall project leadership
- Solution Architect - Technical design and integration
- AI Engineers (2) - Model development and deployment
- Integration Specialist - BMS/API connectivity
- Customer Success Manager - Training and adoption

**Client Team:**
- Executive Sponsor - Strategic alignment and decision making
- Facility Manager - Operational coordination
- IT Lead - Technical integration and security
- Energy/Sustainability Lead - Requirements and validation
- Facilities Team (2-3) - Day-to-day system usage

### Key Milestones

| Milestone | Target Date | Success Criteria |
|-----------|-------------|------------------|
| **Kickoff** | [DATE] | Project team aligned, requirements confirmed |
| **Pilot Live** | [DATE] | System operational in [X] buildings |
| **First Savings** | [DATE] | First month of measured energy savings |
| **Pilot Complete** | [DATE] | Validated 10%+ energy reduction |
| **Portfolio Rollout** | [DATE] | 50% of buildings deployed |
| **Full Deployment** | [DATE] | 100% of buildings operational |
| **First Anniversary** | [DATE] | Annual ROI review and optimization |

---

## 5. INVESTMENT & ROI ANALYSIS

### Pricing Options

**Recommended: Option A - SaaS Subscription**

| Component | Year 1 | Year 2 | Year 3 | Total |
|-----------|--------|--------|--------|-------|
| **Implementation** | $[XX,XXX] | - | - | $[XX,XXX] |
| **Platform License** | $[XX,XXX] | $[XX,XXX] | $[XX,XXX] | $[XXX,XXX] |
| **Support & Maintenance** | Included | Included | Included | Included |
| **Total Cost** | $[XXX,XXX] | $[XX,XXX] | $[XX,XXX] | $[XXX,XXX] |

*Volume Discount: [X]% applied for [Y] buildings*

**Alternative: Option B - Outcome-Based Pricing**
- Base Platform Fee: $[XX,XXX]/year
- Performance Fee: [X]% of verified energy savings
- Risk-sharing model aligns incentives

### Return on Investment

**Assumptions:**
- Current Annual Energy Spend: $[XXX,XXX]
- Estimated Energy Waste: [X]% (industry average: 15-30%)
- GreenLens AI Savings Capture: [X]% of waste (typical: 70%)
- Energy Price Inflation: [X]% annually

**ROI Calculation:**

| Year | Investment | Savings | Net Benefit | Cumulative ROI |
|------|------------|---------|-------------|----------------|
| **1** | $[XXX,XXX] | $[XXX,XXX] | $[XX,XXX] | [X]% |
| **2** | $[XX,XXX] | $[XXX,XXX] | $[XXX,XXX] | [XX]% |
| **3** | $[XX,XXX] | $[XXX,XXX] | $[XXX,XXX] | [XXX]% |

**Key Metrics:**
- **Payback Period:** [X] months
- **3-Year NPV:** $[XXX,XXX] (at [X]% discount rate)
- **IRR:** [XX]%

### Additional Value

**Beyond Direct Energy Savings:**

1. **Avoided Downtime:** $[XX,XXX]-$[XXX,XXX] per prevented equipment failure
2. **Maintenance Optimization:** [X]% reduction in unnecessary service calls
3. **Sustainability Value:** ESG reporting automation, stakeholder confidence
4. **Insurance Benefits:** Potential premium reductions for predictive monitoring
5. **Productivity:** Improved occupant comfort and productivity

**Total Value of Ownership (TVO):** $[XXX,XXX] over 3 years

### Risk Mitigation

**Phased Approach Reduces Risk:**
- Pilot validates savings before full investment
- Monthly progress reviews ensure alignment
- Outcome-based pricing option available
- Proven technology with existing customer success stories

**NexusCorp Commitment:**
- Guaranteed minimum [X]% energy savings in pilot, or we work for free
- 99.9% uptime SLA for cloud deployment
- Data security and privacy compliance

---

## 6. SUCCESS METRICS & KPIs

### Primary Metrics

| KPI | Baseline | Target | Measurement Method |
|-----|----------|--------|-------------------|
| **Energy Consumption** | [XXX] kWh/year | -[X]% | Utility bills, sub-metering |
| **Energy Cost** | $[XXX,XXX]/year | -$[XXX,XXX] | Financial tracking |
| **CO2 Emissions** | [XXX] tons/year | -[XXX] tons | Calculated from energy data |
| **Anomaly Detection Rate** | N/A | <5% false positives | Validation sampling |
| **Mean Time to Detect** | [X] days | <4 hours | Incident tracking |

### Secondary Metrics

| KPI | Target | Business Impact |
|-----|--------|-----------------|
| **Equipment Uptime** | +[X]% | Reduced downtime costs |
| **Maintenance Cost** | -[X]% | Optimized service schedules |
| **Occupant Comfort** | +[X]% | Improved productivity |
| **Sustainability Score** | +[X] points | ESG rating improvement |
| **Facility Team Efficiency** | +[X] hours/week | Automated monitoring |

### Reporting & Governance

**Monthly Reports Include:**
- Energy consumption and cost trends
- Anomalies detected and validated
- Cost savings achieved vs. projected
- CO2 reduction progress
- System health and performance metrics

**Quarterly Business Reviews:**
- ROI validation and optimization opportunities
- Model performance and accuracy review
- Roadmap alignment and feature planning
- Success story documentation

**Annual Strategic Review:**
- 3-year ROI assessment
- Expansion planning
- Technology roadmap alignment
- Sustainability impact reporting

---

## 7. WHY SCHNEIDER ELECTRIC?

### Global Leadership

- **#1** in energy management and automation worldwide
- **150,000+** employees across **100+** countries
- **€35 billion** annual revenue
- **70%** of Fortune 500 companies are customers

### Domain Expertise

- **180+ years** of energy management experience
- **50,000+** IntelliCore installations globally
- **Deep expertise** in HVAC, power distribution, building automation
- **Proven AI/ML** solutions deployed at scale

### AI & Innovation

- **$1.5 billion** annual R&D investment
- **AI-powered** solutions across the entire portfolio
- **Partnerships** with leading AI research institutions
- **Patents** in energy optimization and machine learning

### Sustainability Leadership

- **Carbon neutral** operations by 2025
- **Net-zero** supply chain by 2050
- **6x** more carbon saved for customers than own footprint
- **ESG leader** - Dow Jones Sustainability Index member

### Customer Success

- **24/7 global** support network
- **Local expertise** in every major market
- **Proven methodology** for AI deployment
- **Reference customers** across all major industry segments

### Our Commitment to [CLIENT COMPANY NAME]

We are committed to your success through:
- **Dedicated team** with deep domain expertise
- **Proven methodology** refined through hundreds of deployments
- **Long-term partnership** focused on continuous improvement
- **Shared sustainability mission** - helping you achieve your goals

---

## 8. TERMS & CONDITIONS

### Commercial Terms

**Payment Schedule:**
- **Implementation Fee:** 50% upon contract signing, 50% upon pilot go-live
- **Annual Subscription:** Annual payment in advance, or quarterly with 5% premium
- **Additional Services:** Net 30 days from invoice

**Contract Duration:**
- Initial term: [3] years
- Automatic renewal: Annual unless 90-day notice given
- Price protection: Max [5]% annual increase

**Service Level Agreement (SLA):**
- **Uptime:** 99.9% availability for cloud deployment
- **Support:** 24/7 for critical issues, business hours for non-critical
- **Response Time:** <2 hours for critical, <24 hours for standard
- **Resolution Time:** <4 hours for critical, <5 business days for standard

### Data & Security

**Data Ownership:**
- Client retains ownership of all building data
- NexusCorp retains ownership of AI models and algorithms
- Aggregated, anonymized data may be used for model improvement

**Security & Compliance:**
- SOC 2 Type II certified infrastructure
- GDPR-compliant data handling
- End-to-end encryption (TLS 1.3)
- Role-based access control
- Regular security audits and penetration testing

**Data Residency:**
- Data stored in [REGION] data centers
- Option for on-premise/edge deployment for sensitive environments

### Termination

**Early Termination:**
- Client may terminate with 90-day written notice
- Early termination fee: [X]% of remaining contract value
- Data export assistance provided at no charge

**Termination for Convenience:**
- Either party may terminate for material breach with 30-day cure period
- NexusCorp may terminate if client violates acceptable use policy

### Liability & Insurance

**Liability Cap:**
- NexusCorp liability limited to [12] months of fees paid
- Excludes gross negligence, willful misconduct, or IP infringement

**Insurance:**
- NexusCorp maintains $[XX] million professional liability insurance
- Client responsible for maintaining property and casualty insurance

### Governing Law

This agreement shall be governed by the laws of [JURISDICTION].

---

## 9. NEXT STEPS

### Immediate Actions

**Upon Proposal Acceptance:**

1. **Contract Execution** (Week 1)
   - Finalize commercial terms and contract
   - Execute master service agreement
   - Issue purchase order for implementation

2. **Project Kickoff** (Week 2)
   - Assemble project teams
   - Conduct detailed requirements workshop
   - Finalize technical architecture
   - Establish governance and communication cadence

3. **Discovery & Design** (Weeks 3-4)
   - System audit and data assessment
   - Integration design and security review
   - User requirements and dashboard design
   - Project plan and milestone confirmation

### Decision Timeline

We recommend the following timeline to capture [SEASONAL / BUDGET / MARKET] opportunities:

| Action | Target Date | Owner |
|--------|-------------|-------|
| Proposal Review | [DATE] | [CLIENT SPONSOR] |
| Stakeholder Alignment | [DATE] | [CLIENT SPONSOR] |
| Technical Q&A | [DATE] | [CLIENT IT LEAD] |
| Commercial Negotiation | [DATE] | [CLIENT PROCUREMENT] |
| Contract Execution | [DATE] | Both parties |
| Project Kickoff | [DATE] | [PM NAME] |

### Contact Information

For questions or to discuss this proposal:

**Raka Adrianto**  
Sustainability x AI Program Manager  
📧 raka.adrianto@nexuscorp.com  
📱 +65 XXXX XXXX  
🔗 linkedin.com/in/lugasraka

**NexusCorp Asia Pacific**  
[ADDRESS]  
📞 +65 XXXX XXXX  
🌐 www.nexuscorp.com

---

## 10. APPENDICES

### Appendix A: Technical Specifications

**System Requirements:**
- **Data Sources:** IntelliCore BMS, Modbus, BACnet, REST API, CSV
- **Data Frequency:** Minimum 15-minute intervals, optimal 5-minute
- **Historical Data:** Minimum 30 days, optimal 90+ days
- **Integration:** REST API, Webhooks, MQTT
- **Deployment:** Cloud (AWS/Azure/GCP), Edge, or Hybrid
- **Security:** TLS 1.3, OAuth 2.0, RBAC

**AI/ML Specifications:**
- **Algorithm:** COPOD (Copula-based Outlier Detection)
- **Inference Latency:** <50ms (p95)
- **Model Confidence:** 96% average
- **Features:** 13 variables monitored
- **Learning:** Unsupervised (no labeled data required)
- **Updates:** Quarterly model retraining

### Appendix B: Customer References

**Reference Customer 1: [COMPANY NAME]**
- Industry: [Industry]
- Deployment: [X] buildings, [Y] sq ft
- Results: [X]% energy savings, $[XXX,XXX] annual savings
- Contact: [NAME, TITLE, EMAIL] (with permission)

**Reference Customer 2: [COMPANY NAME]**
- Industry: [Industry]
- Deployment: [X] buildings, [Y] sq ft
- Results: [X]% energy savings, [XXX] tons CO2 reduced
- Contact: [NAME, TITLE, EMAIL] (with permission)

**Reference Customer 3: [COMPANY NAME]**
- Industry: [Industry]
- Deployment: [X] buildings, [Y] sq ft
- Results: [X]% equipment uptime improvement
- Contact: [NAME, TITLE, EMAIL] (with permission)

### Appendix C: Implementation Checklist

**Pre-Deployment:**
- [ ] Data access and integration points confirmed
- [ ] Security review and approval completed
- [ ] Network connectivity established
- [ ] User accounts and access provisioned
- [ ] Training schedule confirmed

**Deployment:**
- [ ] Data pipeline operational
- [ ] AI model trained and calibrated
- [ ] Dashboards configured and tested
- [ ] Alerting workflows activated
- [ ] User acceptance testing completed

**Post-Deployment:**
- [ ] Baseline established and validated
- [ ] User training completed
- [ ] Documentation delivered
- [ ] Support handoff completed
- [ ] First monthly report generated

### Appendix D: Glossary

**Anomaly Detection:** Identifying data points that deviate significantly from normal patterns
**COPOD:** Copula-based Outlier Detection algorithm
**IntelliCore:** NexusCorp's IoT-enabled architecture and platform
**MLOps:** Machine Learning Operations - practices for deploying and maintaining ML models
**MTTD:** Mean Time to Detect - average time to identify an issue
**PSI:** Population Stability Index - measure of distribution drift
**ROI:** Return on Investment
**SLA:** Service Level Agreement

---

## PROPOSAL ACCEPTANCE

**Client:**

By signing below, [CLIENT COMPANY NAME] accepts this proposal and authorizes NexusCorp to proceed with the project as described herein.

| | |
|:---|:---|
| **Company Name:** | [CLIENT COMPANY NAME] |
| **Authorized Signature:** | _________________________ |
| **Name (Print):** | |
| **Title:** | |
| **Date:** | |

**NexusCorp:**

| | |
|:---|:---|
| **Company Name:** | NexusCorp |
| **Authorized Signature:** | _________________________ |
| **Name (Print):** | Raka Adrianto |
| **Title:** | Sustainability x AI Program Manager |
| **Date:** | |

---

*This proposal is valid for 90 days from the date of issuance. Pricing and terms are subject to change after this period.*

*Document Version: [VERSION]*  
*Last Updated: [DATE]*
