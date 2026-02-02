# Stakeholder Communication Guides
## GreenLens AI - Tailored Messaging for Different Audiences

---

## 1. Executive Audience (C-Suite, Board Members)

### Key Messages

**Primary Focus:** Business outcomes, financial returns, competitive advantage

**Time Allocation:** 15-20 minutes maximum

**Core Message:**
> "GreenLens AI transforms energy from a cost center into a competitive advantage, delivering 15-20% energy savings with 12-month payback while advancing your sustainability commitments."

### What Executives Care About

1. **Financial Performance**
   - ROI and payback period
   - Impact on EBITDA
   - Risk-adjusted returns
   - Total Cost of Ownership (TCO)

2. **Strategic Value**
   - Competitive differentiation
   - Market positioning
   - Innovation leadership
   - ESG ratings improvement

3. **Risk Management**
   - Implementation risk mitigation
   - Technology obsolescence
   - Vendor stability
   - Data security

### Communication Approach

**Lead With:**
- Financial metrics (ROI, NPV, payback)
- Business outcomes (cost savings, CO2 reduction)
- Strategic alignment (sustainability goals, digital transformation)

**Avoid:**
- Technical jargon (algorithms, APIs, data pipelines)
- Implementation details
- Feature lists without business context

**Sample Opening:**
> "Good morning. Today I'll show you how we can reduce your energy costs by $500,000 annually while cutting 600 tons of CO2 emissions - achieving payback in just 12 months through AI-powered building optimization."

### Key Statistics to Emphasize

- **18%** average energy reduction
- **$2,000-$10,000** annual savings per building
- **12-month** typical payback period
- **180%** 3-year ROI
- **30%** faster problem detection vs. traditional systems

### Executive Q&A Preparation

**Q: "What's the total investment?"**
A: "Implementation starts at $75,000 with annual subscriptions of $25,000 per building. For a 5-building portfolio, you're looking at $200,000 first-year investment generating $300,000+ in annual savings - 150% first-year ROI."

**Q: "How is this different from our existing BMS?"**
A: "Your BMS tells you temperature; GreenLens AI tells you 'your damper is stuck.' We add an intelligence layer that correlates multiple data points to detect contextual anomalies - reducing false alarms by 80% and catching issues 30% faster."

**Q: "What if it doesn't work?"**
A: "We start with a pilot in 1-2 buildings to prove value before scaling. Our pilot success rate is 95%, and we offer outcome-based pricing where we share the risk. If we don't deliver the projected savings, you don't pay the full subscription."

**Q: "How does this impact our sustainability goals?"**
A: "Typical deployment reduces CO2 by 400-800 tons annually per building. This directly supports net-zero commitments and improves ESG ratings - many clients see 10-15 point improvements in sustainability scores."

---

## 2. Technical Audience (IT, Engineering, Solution Architects)

### Key Messages

**Primary Focus:** Architecture, integration, security, scalability

**Time Allocation:** 45-60 minutes with deep-dive capability

**Core Message:**
> "GreenLens AI is built on enterprise-grade architecture with native IntelliCore integration, SOC 2 compliance, and MLOps monitoring - designed for production deployment at scale."

### What Technical Stakeholders Care About

1. **Architecture & Integration**
   - System architecture and data flow
   - API specifications and protocols
   - Integration complexity
   - Legacy system compatibility

2. **Security & Compliance**
   - Data encryption and residency
   - Access controls and authentication
   - Compliance certifications
   - Security audit trails

3. **Performance & Scalability**
   - Latency and throughput
   - High availability architecture
   - Disaster recovery
   - Scalability limits

4. **Operational Excellence**
   - MLOps and model management
   - Monitoring and alerting
   - Maintenance requirements
   - Support model

### Communication Approach

**Lead With:**
- Technical architecture diagrams
- Integration patterns and APIs
- Security architecture and certifications
- Performance benchmarks

**Provide:**
- Detailed technical documentation
- API specifications
- Security whitepapers
- Reference architectures

**Sample Opening:**
> "I'll walk you through our technical architecture, integration patterns, and security model. GreenLens AI uses a microservices architecture deployed on Kubernetes, with sub-50ms inference latency and 99.9% uptime SLA."

### Technical Deep-Dive Topics

**1. AI/ML Architecture**
```
Algorithm: COPOD (Copula-based Outlier Detection)
- Unsupervised learning (no labeled data required)
- Handles multivariate correlations (13 features)
- Inference latency: <50ms (p95)
- Model confidence: 96% average
- Automatic retraining quarterly
```

**2. Integration Patterns**
```
Data Ingestion:
- REST API (JSON/CSV)
- MQTT for IoT streams
- IntelliCore Building Management native connector
- Modbus/BACnet gateway support

Deployment Options:
- Cloud: AWS/Azure/GCP
- Edge: On-premise Kubernetes
- Hybrid: Edge inference + Cloud training
```

**3. Security Architecture**
```
- TLS 1.3 for data in transit
- AES-256 for data at rest
- OAuth 2.0 + RBAC for access control
- SOC 2 Type II certified
- GDPR compliant
- Data residency options (SG, EU, US)
```

### Technical Q&A Preparation

**Q: "How does it integrate with our existing IntelliCore deployment?"**
A: "We provide a native IntelliCore Building Management connector that uses the existing IBM data model. Installation is typically 2-3 days with no custom development required. We can also integrate via REST API if you prefer."

**Q: "What are the infrastructure requirements?"**
A: "For cloud deployment: none - we host on AWS Singapore. For edge deployment: Kubernetes cluster with 4 vCPU, 16GB RAM per instance. Data storage: approximately 1GB per building per year."

**Q: "How do you handle model drift and accuracy?"**
A: "We implemented full MLOps monitoring with automated drift detection using PSI (Population Stability Index). If drift exceeds thresholds, we trigger model retraining. Performance dashboards track latency, accuracy, and prediction patterns in real-time."

**Q: "What's the API rate limiting?"**
A: "Standard tier: 1,000 requests/minute per building. Enterprise tier: 10,000 requests/minute. We use token bucket algorithm with burst capacity for real-time streaming."

---

## 3. Operational Audience (Facility Managers, Operations Teams)

### Key Messages

**Primary Focus:** Day-to-day usability, workflow integration, actionable insights

**Time Allocation:** 30-45 minutes with hands-on demo

**Core Message:**
> "GreenLens AI makes your job easier by automatically detecting energy waste and telling you exactly what to fix - reducing your manual monitoring time by 70% while catching issues 30% faster."

### What Operations Teams Care About

1. **Ease of Use**
   - Dashboard intuitiveness
   - Alert clarity and actionability
   - Mobile accessibility
   - Training requirements

2. **Workflow Integration**
   - Existing tool compatibility
   - Alert routing (email/SMS/ticketing)
   - Maintenance system integration
   - Reporting automation

3. **Actionable Insights**
   - Root cause identification
   - Recommended actions
   - Priority ranking
   - Validation feedback

4. **Trust & Reliability**
   - False positive rate
   - Accuracy validation
   - System uptime
   - Support responsiveness

### Communication Approach

**Lead With:**
- Live dashboard demonstration
- Real anomaly examples
- Mobile app walkthrough
- Day-in-the-life scenarios

**Emphasize:**
- Time savings (less manual monitoring)
- Early problem detection
- Clear action recommendations
- Validation and feedback loops

**Sample Opening:**
> "Let me show you a typical day with GreenLens AI. Instead of manually checking 50+ energy meters, you get a morning summary: '3 anomalies detected - likely causes: stuck damper in Zone B, weekend schedule override in Lobby.' You click, verify, dispatch maintenance. Done in 5 minutes."

### Demo Script for Operations

**1. Dashboard Overview (5 min)**
- Show main dashboard with energy trends
- Highlight anomaly markers (red dots)
- Explain business metrics (cost, CO2)
- Show mobile-responsive design

**2. Anomaly Investigation (10 min)**
- Click on an anomaly
- Show root cause analysis
- Display recommended actions
- Explain confidence score

**3. Alert Configuration (5 min)**
- Show alert routing options
- Demonstrate email/SMS setup
- Explain escalation rules
- Show ticketing system integration

**4. Reporting & Validation (5 min)**
- Show monthly savings report
- Demonstrate feedback mechanism
- Explain model improvement loop
- Show validation workflow

### Operations Q&A Preparation

**Q: "How many false alarms will I get?"**
A: "Our contextual detection reduces false positives to 15% vs. 80% with traditional threshold systems. You can also provide feedback - mark alerts as valid or false - and the system learns your building's patterns to improve accuracy."

**Q: "Can I integrate this with our CMMS?"**
A: "Yes - we provide webhooks and API endpoints to automatically create work orders in your CMMS (ServiceNow, IBM Maximo, etc.). When an anomaly is detected, a ticket is created with the root cause analysis and recommended fix."

**Q: "What happens when I'm off-duty?"**
A: "Alerts can be routed to on-call staff via SMS or phone call for critical issues. Non-critical anomalies are batched into a morning summary email. You set the thresholds and routing rules."

**Q: "How do I know the savings are real?"**
A: "We provide monthly validation reports comparing actual energy consumption against baseline. You can also input utility bills for cross-validation. Most clients see measurable savings within 30 days of deployment."

---

## 4. Financial Audience (CFO, Procurement, Finance Teams)

### Key Messages

**Primary Focus:** Cost justification, budget impact, risk-adjusted returns

**Time Allocation:** 20-30 minutes with financial models

**Core Message:**
> "GreenLens AI delivers 180% 3-year ROI with 12-month payback, turning energy waste into bottom-line profit while providing predictable operating expenses through our SaaS model."

### What Financial Stakeholders Care About

1. **Return on Investment**
   - Payback period
   - NPV and IRR
   - Cash flow impact
   - Sensitivity analysis

2. **Cost Structure**
   - Capex vs. Opex
   - Pricing model clarity
   - Hidden costs
   - Volume discounts

3. **Risk Assessment**
   - Implementation risk
   - Technology risk
   - Vendor financial stability
   - Contract terms

4. **Budget Planning**
   - Year-over-year costs
   - Scaling costs
   - Contract flexibility
   - Payment terms

### Communication Approach

**Lead With:**
- ROI calculator demonstration
- Financial projections
- Risk mitigation strategies
- Flexible pricing options

**Provide:**
- Detailed financial model (Excel)
- Sensitivity analysis
- Scenario comparisons
- Reference customer financials

**Sample Opening:**
> "From a financial perspective, GreenLens AI represents a low-risk, high-return investment. For a 5-building portfolio, you're investing $200,000 in year one to generate $300,000 in annual savings - that's 150% first-year ROI and 12-month payback."

### Financial Presentation Structure

**1. Investment Summary (5 min)**
- Total cost breakdown
- Year-by-year cash flow
- Cumulative ROI curve
- Payback period visualization

**2. Scenario Analysis (10 min)**
- Conservative (12% waste, 60% capture)
- Expected (18% waste, 70% capture)
- Optimistic (25% waste, 80% capture)
- Sensitivity to energy prices

**3. Risk Mitigation (5 min)**
- Pilot approach reduces risk
- Outcome-based pricing option
- Performance guarantees
- Flexible contract terms

**4. Budget Impact (5 min)**
- Opex vs. Capex benefits
- Predictable annual costs
- Volume discount structure
- Multi-year contract advantages

### Financial Q&A Preparation

**Q: "What's the total cost of ownership over 5 years?"**
A: "For a 5-building portfolio: Year 1: $200K (implementation + subscription), Years 2-5: $125K annually. Total 5-year investment: $700K. Total 5-year savings: $1.8M. Net benefit: $1.1M. ROI: 257%."

**Q: "Can we do outcome-based pricing?"**
A: "Yes - we offer a performance model with a base platform fee of $15K per building plus 20% of verified energy savings. This aligns our incentives with your outcomes and reduces your upfront risk."

**Q: "How do you verify the savings?"**
A: "We use the International Performance Measurement and Verification Protocol (IPMVP). Monthly reports compare actual consumption against weather-normalized baseline. Independent auditors can validate our calculations."

**Q: "What are the contract terms?"**
A: "Standard is 3-year initial term with annual renewals. We offer: 90-day termination for convenience (with fee), annual payment (3% discount for upfront), and price protection (max 5% annual increase)."

---

## 5. Sustainability Audience (Sustainability Officers, ESG Teams)

### Key Messages

**Primary Focus:** Environmental impact, ESG reporting, sustainability goals

**Time Allocation:** 20-30 minutes with impact metrics

**Core Message:**
> "GreenLens AI transforms your building operations into a sustainability success story, delivering measurable CO2 reductions of 400-800 tons per building annually while automating ESG reporting and supporting net-zero commitments."

### What Sustainability Teams Care About

1. **Environmental Impact**
   - CO2 reduction quantification
   - Carbon footprint improvement
   - Resource efficiency
   - Circular economy alignment

2. **ESG Reporting**
   - Automated data collection
   - GRI/SASB alignment
   - Stakeholder reporting
   - Third-party verification

3. **Goal Alignment**
   - Net-zero pathway
   - Science-based targets
   - SDG contributions
   - Industry benchmarks

4. **Credibility & Transparency**
   - Measurement methodology
   - Audit trails
   - Third-party validation
   - Industry recognition

### Communication Approach

**Lead With:**
- CO2 reduction metrics
- ESG reporting automation
- Sustainability story
- Industry leadership

**Provide:**
- Sustainability impact report
- ESG data templates
- Case studies from similar companies
- Certification documentation

**Sample Opening:**
> "GreenLens AI directly supports your net-zero commitment by eliminating 400-800 tons of CO2 per building annually - equivalent to taking 175 cars off the road. More importantly, it automates your ESG data collection and provides auditable sustainability reports for stakeholders."

### Sustainability Metrics to Highlight

**Environmental Impact:**
- **400-800 tons CO2** reduction per building annually
- **15-20%** energy consumption reduction
- **Equivalent impact:** 175-350 cars removed from roads
- **Water savings:** Reduced cooling tower usage

**ESG Benefits:**
- Automated Scope 2 emissions tracking
- GRI 302 (Energy) and GRI 305 (Emissions) alignment
- Real-time sustainability dashboards
- Stakeholder-ready reports

**Strategic Value:**
- Supports Science-Based Targets (SBTi)
- Contributes to UN SDG 7 (Affordable Clean Energy)
- Improves CDP and DJSI scores
- Enhances green building certifications (LEED, BREEAM)

### Sustainability Q&A Preparation

**Q: "How do you calculate CO2 reductions?"**
A: "We use the GHG Protocol methodology. For each kWh of energy saved, we apply your regional grid emission factor (configurable: 0.2-0.8 kg CO2/kWh). Reductions are Scope 2 and can be verified by third-party auditors."

**Q: "Can this help with our CDP submission?"**
A: "Yes - we provide automated data collection for CDP Climate Change questions CC8.2a (energy consumption) and CC9.1 (emissions reduction activities). Our reports are structured to match CDP requirements."

**Q: "How does this support Science-Based Targets?"**
A: "The 15-20% reduction in building energy directly contributes to your absolute or intensity-based targets. We provide forward-looking projections showing how GreenLens AI accelerates your pathway to 1.5°C alignment."

**Q: "Can we use this for marketing/PR?"**
A: "Absolutely - we provide impact certificates quarterly showing your CO2 reduction. Many clients feature these in sustainability reports, press releases, and stakeholder communications. We can also provide joint case studies."

---

## 6. Sales Team Enablement

### Key Messages

**Primary Focus:** Value proposition, objection handling, competitive positioning

**Time Allocation:** 60-minute training session

**Core Message:**
> "GreenLens AI is the easiest AI solution to sell - it has clear ROI, quick time-to-value, and integrates seamlessly with IntelliCore. Lead with business outcomes, not technical features."

### Sales Playbook Overview

**1. Ideal Customer Profile (ICP)**

**Best Fit:**
- 5+ buildings in portfolio
- $500K+ annual energy spend
- Existing IntelliCore or BMS deployment
- Sustainability goals or mandates
- Facility management team >3 people

**Good Fit:**
- 2-4 buildings
- $200K+ annual energy spend
- Manual monitoring today
- High energy costs (>$0.15/kWh)

**Poor Fit:**
- Single small building (<50K sq ft)
- No BMS or data infrastructure
- Low energy costs (<$0.08/kWh)
- No sustainability pressure

**2. Discovery Questions**

**Business Questions:**
- "What's your annual energy spend across the portfolio?"
- "Do you have sustainability targets or ESG reporting requirements?"
- "How do you currently identify energy waste or equipment issues?"
- "What's your biggest pain point in facility management today?"

**Technical Questions:**
- "What building management system do you use?"
- "How do you collect energy data today?"
- "Do you have IntelliCore deployed?"
- "What's your cloud vs. on-premise preference?"

**Financial Questions:**
- "What's your typical capital approval process?"
- "Do you prefer CapEx or OpEx models?"
- "What ROI threshold do you need to justify investments?"
- "Are you open to pilot programs to prove value?"

**3. Value Proposition by Role**

| Role | Primary Value | Key Message |
|------|---------------|-------------|
| **CEO/Board** | Competitive advantage | "Turn energy into strategic advantage" |
| **CFO** | Financial returns | "180% ROI, 12-month payback" |
| **COO** | Operational efficiency | "30% faster issue detection" |
| **CIO** | Digital transformation | "AI-powered building optimization" |
| **CSO** | Sustainability | "400-800 tons CO2 reduction annually" |
| **VP Facilities** | Team productivity | "70% reduction in manual monitoring" |
| **Facility Manager** | Daily workflow | "Know exactly what to fix and when" |
| **Energy Manager** | Data & insights | "Automated anomaly detection and root cause" |

**4. Competitive Positioning**

**vs. Traditional BMS:**
- "BMS tells you temperature; we tell you what's broken"
- "80% fewer false alarms"
- "No manual threshold tuning required"

**vs. Generic AI Platforms:**
- "Built specifically for buildings and energy"
- "IntelliCore native integration"
- "Domain expertise from 180+ years in energy"

**vs. Point Solutions:**
- "Unified platform for entire portfolio"
- "Scales from 1 to 1,000 buildings"
- "Single vendor accountability"

**5. Objection Handling**

**"We already have a BMS"**
Response: "Perfect - GreenLens AI complements your BMS by adding an AI intelligence layer. Think of it as going from a speedometer to a diagnostic system. We integrate seamlessly and enhance what you already have."

**"AI seems complex"**
Response: "We've made it simple. The AI is unsupervised - it learns your building's normal patterns automatically. No data labeling, no complex setup. Most pilots are live within 2 weeks."

**"What's the payback?"**
Response: "Typical payback is 12 months with 180% 3-year ROI. But let's calculate your specific scenario - what's your annual energy spend? [Use ROI calculator]"

**"We don't have budget"**
Response: "I understand. Many clients start with a single-building pilot using outcome-based pricing - you pay a percentage of verified savings. This requires minimal upfront investment and proves value before scaling."

**"We need to think about it"**
Response: "Of course. To help you evaluate, I'd suggest: (1) Discovery workshop to assess your buildings, (2) ROI calculation specific to your portfolio, (3) Reference calls with similar customers. Which would be most helpful?"

**6. Closing Techniques**

**Assumptive Close:**
"Based on your 10-building portfolio, you're looking at $600K annual savings. Which two buildings should we start the pilot with?"

**Alternative Close:**
"Would you prefer to start with the standard SaaS model or the outcome-based pricing option?"

**Puppy Dog Close:**
"Let's run a 30-day pilot in one building at no cost. You'll see real anomalies and savings within the first week. If you don't see value, we part as friends."

**Time-Limited Close:**
"We're offering 20% volume discounts for commitments made this quarter. Shall we schedule the discovery workshop for next week to secure this pricing?"

---

## 7. FAQ Document

### General Questions

**Q: What is GreenLens AI?**
A: GreenLens AI is an intelligent anomaly detection system that monitors building energy consumption and identifies operational inefficiencies in real-time. It uses advanced AI to detect contextual anomalies (e.g., high energy use during cool weather indicating stuck dampers) and translates them into financial impact and CO2 reduction metrics.

**Q: How long does implementation take?**
A: Pilot deployment: 4-6 weeks. Full portfolio rollout: 3-6 months depending on building count. Single building can be live in 2-3 weeks.

**Q: Do we need to replace our existing BMS?**
A: No - GreenLens AI integrates with your existing BMS (IntelliCore, Honeywell, Siemens, etc.) and adds an AI intelligence layer on top.

### Technical Questions

**Q: What data does it need?**
A: Minimum: Energy consumption and outdoor temperature. Optimal: 13 variables including occupancy, HVAC status, humidity, solar irradiance. Data frequency: 15-minute intervals.

**Q: How accurate is the AI?**
A: 96% average confidence score. False positive rate: 15% (vs. 80% for threshold-based systems). Accuracy improves over time as the system learns your building's patterns.

**Q: Is our data secure?**
A: Yes - SOC 2 Type II certified, GDPR compliant, TLS 1.3 encryption, OAuth 2.0 authentication. Data residency options available (Singapore, EU, US).

### Financial Questions

**Q: What's the pricing model?**
A: SaaS subscription: $15K-$35K per building annually (volume discounts available). Includes implementation, training, support, and updates. Outcome-based pricing also available.

**Q: What's the typical ROI?**
A: 180% 3-year ROI with 12-month payback. Conservative scenario: 120% ROI. Optimistic: 250% ROI.

**Q: Are there hidden costs?**
A: No - subscription includes everything except optional add-ons (predictive maintenance integration, automated controls, custom reporting).

### Operational Questions

**Q: How will this change my team's workflow?**
A: Reduces manual monitoring time by 70%. Instead of checking meters, your team receives prioritized anomaly alerts with root cause analysis and recommended actions.

**Q: What training is required?**
A: Minimal - 2-hour training session for facility team. Dashboard is intuitive and mobile-responsive. Most users are proficient within a week.

**Q: How do we validate the savings?**
A: Monthly reports compare actual consumption against baseline. You can input utility bills for cross-validation. Independent auditors can verify calculations using IPMVP protocol.

### Sustainability Questions

**Q: How much CO2 can we reduce?**
A: 400-800 tons per building annually (typical). Depends on building size, current waste, and grid emission factor.

**Q: Does this support our ESG reporting?**
A: Yes - automated data collection for GRI, SASB, CDP. Provides auditable sustainability reports and impact certificates.

**Q: Can we use this for carbon credits?**
A: Potentially - the CO2 reductions are measurable and verifiable. Consult with your carbon credit provider to confirm eligibility.

---

## 8. Communication Best Practices

### Do's

✅ **Lead with outcomes, not features**
- "Reduce energy costs by 18%" vs. "Uses COPOD algorithm"

✅ **Use customer language**
- "Stuck damper" not "anomalous correlation coefficient"

✅ **Quantify everything**
- "$500K savings" not "significant cost reduction"

✅ **Tell stories**
- Share specific customer examples with real numbers

✅ **Address the "so what"**
- Connect every feature to business value

✅ **Use visuals**
- Dashboard screenshots, ROI charts, architecture diagrams

✅ **Prepare for skepticism**
- Have proof points, references, and pilot options ready

### Don'ts

❌ **Don't use jargon**
- Avoid: "unsupervised learning," "copula functions," "multivariate analysis"

❌ **Don't oversell**
- Use conservative estimates, not best-case scenarios

❌ **Don't ignore concerns**
- Address objections head-on with data

❌ **Don't rush to close**
- Build trust first, especially with technical audiences

❌ **Don't be generic**
- Customize for industry, role, and use case

❌ **Don't forget follow-up**
- Send summary, ROI calculator, and next steps within 24 hours

### Meeting Structure Template

**Executive Meeting (30 min):**
1. Opening (2 min): Hook with business outcome
2. Problem (3 min): Industry context and pain points
3. Solution (5 min): High-level capabilities
4. Proof (10 min): ROI, case studies, references
5. Investment (5 min): Pricing and commercial terms
6. Next Steps (5 min): Clear action items

**Technical Deep-Dive (60 min):**
1. Architecture (15 min): System design and integration
2. Security (10 min): Compliance and data protection
3. Demo (20 min): Live dashboard walkthrough
4. Q&A (15 min): Technical questions and concerns

**Discovery Workshop (90 min):**
1. Introductions (10 min): Team and objectives
2. Current State (20 min): Existing systems and challenges
3. Requirements (30 min): Technical and business needs
4. Solution Fit (20 min): How GreenLens AI addresses needs
5. Next Steps (10 min): Proposal and pilot planning

---

## 9. Reference Materials

### Templates Available

1. **Sales Presentation Deck** (`sales_deck/GreenLens_AI_Sales_Deck.md`)
   - 12-slide presentation for customer meetings
   - Speaker notes and objection handling
   - Appendix with technical details

2. **Customer Proposal Template** (`proposal_template/Customer_Proposal_Template.md`)
   - Comprehensive proposal structure
   - Customizable for specific opportunities
   - Includes terms and acceptance form

3. **ROI Calculator** (`pages/02_ROI_Calculator.py`)
   - Interactive Streamlit application
   - Scenario analysis and sensitivity testing
   - Excel export capability

4. **Communication Guides** (this document)
   - Audience-specific messaging
   - Q&A preparation
   - Best practices and templates

### Quick Reference Card

**Elevator Pitch (30 seconds):**
> "GreenLens AI is an intelligent building optimization system that uses AI to detect energy waste in real-time. It identifies issues like stuck dampers or schedule overrides automatically, delivering 15-20% energy savings with 12-month payback. Think of it as a diagnostic system for your building's energy health."

**One-Pager Summary:**
- **What:** AI-powered anomaly detection for buildings
- **Benefit:** 15-20% energy savings, $2K-$10K per building annually
- **Differentiator:** Contextual detection vs. simple thresholds
- **Integration:** IntelliCore native, 2-week deployment
- **ROI:** 180% 3-year return, 12-month payback

**Contact for Questions:**
Raka Adrianto, Sustainability x AI Program Manager  
raka.adrianto@nexuscorp.com | +65 XXXX XXXX

---

*Document Version: 1.0*  
*Last Updated: February 2026*  
*For Internal Sales & Customer-Facing Teams*
