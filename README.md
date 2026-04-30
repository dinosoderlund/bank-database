# Bank Database

A bank database built in SQL Server simulating core banking operations 
with real-time event ingestion, audit logging, and fraud detection.

## Features

### SQL
- Tables for customers, accounts, loans, transactions, and services
- Audit logging system to track user activity
- Views for session analysis and anomaly detection
- Fraud detection view flagging IPs with 5+ login failures within 5 minutes

### Python
- `producer.py` → simulates real-time customer events using Faker and writes them into the database
- `dashboard.py` → Streamlit dashboard with live event table, action chart and fraud indicator
- `main.py` → FastAPI REST API exposing database views via HTTP endpoints

## Getting Started

1. Clone the repo
2. Set up SQL Server and run the schema scripts
3. Install dependencies:
```
pip install faker pypyodbc streamlit pandas fastapi uvicorn
```
4. Run the producer:
```
python producer.py
```
5. Run the dashboard:
```
python -m streamlit run dashboard.py
```
6. Run the API:
```
python -m uvicorn main:app --reload
```

API docs available at `http://localhost:8000/docs`

## Docker

Build and run the API in a Docker container:
```
docker build -t bank-api .
docker run -p 8000:8000 --add-host=host.docker.internal:host-gateway bank-api
```

## CI/CD

GitHub Actions automatically builds the Docker image on every push and pull request to main.

## Planned Features
- Stream processing with Kafka or Azure Event Hubs
- Fraud detection model on top of the anomaly detection views