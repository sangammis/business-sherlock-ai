# 🔎 Business Sherlock AI

## Autonomous Business Investigation Agent

Business Sherlock AI is an AI-powered investigation agent that automatically identifies the root causes of business incidents by analyzing evidence across multiple enterprise data sources.

Instead of simply answering questions, the agent plans an investigation, gathers evidence from Elastic, reasons over the findings using Gemini, and generates a professional investigation report with business impact analysis and recommendations.

Built for the **Google Gemini + Elastic MCP Hackathon**.

---

# 🚀 Problem Statement

Business teams often struggle to identify the root causes behind:

* Revenue declines
* Payment failures
* Application outages
* Customer dissatisfaction
* Shipping and logistics disruptions

Investigations usually require manually analyzing data from multiple systems, consuming hours or even days.

Business Sherlock AI automates this process.

---

# 💡 Solution

Business Sherlock AI acts as an autonomous investigation agent.

Given a business question such as:

> Investigate revenue decline in March

The agent:

1. Determines the investigation type
2. Collects relevant evidence from Elastic
3. Correlates business events, customer reviews, support tickets, and sales data
4. Uses Gemini to perform root-cause analysis
5. Produces a professional investigation report

---

# 🏗 Architecture

User Query
↓
Planner
↓
Evidence Collector
↓
Elastic Search
├── Sales Data
├── Support Tickets
├── Customer Reviews
└── Business Events
↓
Gemini Reasoning Engine
↓
Investigation Report
↓
Streamlit Dashboard

---

# 🧠 Key Features

### Intelligent Investigation Planning

Automatically classifies investigations into:

* Payment Investigations
* Application Investigations
* Shipping Investigations

### Evidence Collection

Retrieves and correlates information from:

* Sales transactions
* Customer reviews
* Support tickets
* Business event logs

### Root Cause Analysis

Uses Gemini to determine:

* Root Cause
* Confidence Level
* Business Impact
* Recommended Actions

### Interactive Dashboard

Streamlit-based UI for business users.

---

# ⚙️ Tech Stack

### AI

* Google Gemini 2.5 Flash

### Search & Analytics

* Elasticsearch

### Backend

* Python

### Frontend

* Streamlit

### Data Processing

* Pandas
* NumPy

---

# 📂 Project Structure

business-sherlock-ai/

agent/
├── planner.py
├── evidence_collector.py
├── reasoning.py
├── gemini_client.py
└── config.py

elastic/
├── elastic_client.py
├── create_indexes.py
├── load_data.py
└── search_queries.py

scripts/
├── generate_sales.py
├── generate_tickets.py
├── generate_reviews.py
├── generate_events.py
└── generate_web_analytics.py

app.py

---

# 📊 Investigation Scenarios

### Revenue Investigation

Query:

Investigate revenue decline in March

Root Cause:

Payment Gateway Upgrade causing checkout failures.

---

### Application Investigation

Query:

Investigate app crashes after release

Root Cause:

Mobile App Release introduced severe performance issues.

---

### Shipping Investigation

Query:

Investigate delivery delays

Root Cause:

Shipping Provider Migration caused logistics disruptions.

---

# 🔍 How Elastic Is Used

Elastic acts as the investigation knowledge layer.

The platform indexes:

* Sales transactions
* Support tickets
* Customer reviews
* Business events

The agent retrieves evidence from Elastic and correlates information across datasets before sending the evidence package to Gemini for analysis.

---

# 🛠 Local Setup

Clone repository:

git clone <repo-url>

Create virtual environment:

python -m venv venv

Activate:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Configure environment variables:

ELASTIC_URL=...
ELASTIC_USERNAME=...
ELASTIC_PASSWORD=...
GEMINI_API_KEY=...

Run Streamlit:

streamlit run app.py

---

# 🎥 Demo

Demo Video:

[Add Devpost Demo Video Link]

---

# 🌐 Live Application

[Add Deployment URL]

---

# 🚧 Future Improvements

* Elastic MCP Integration
* Investigation Memory
* Executive Dashboards
* Real-time Incident Monitoring
* Multi-Agent Collaboration

---

# 📜 License

MIT License

