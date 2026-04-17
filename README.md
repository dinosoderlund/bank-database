# Bank Database

A bank database built in SQL Server simulating core banking operations with real-time event ingestion and audit logging.

---

## Features

### SQL
- Tables for customers, accounts, loans, transactions, and services
- Audit logging system to track user activity
- Views for session analysis and anomaly detection

### Python
- `producer.py` → simulates real-time customer events using Faker and writes them into the database

---

## Getting Started

1. Clone the repo
2. Set up SQL Server and run the schema scripts
3. Install dependencies:
```bash
   pip install faker pyodbc
```
4. Run the producer:
```bash
   python producer.py
```

---

## Planned Features

- REST API layer using FastAPI
- Stream processing with Kafka or Azure Event Hubs
- Fraud detection model on top of the anomaly detection views
- Dashboard for transaction monitoring and session analysis
- Containerize with Docker
- CI/CD pipeline with GitHub Actions