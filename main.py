from fastapi import FastAPI
from database_connect import get_conn

app = FastAPI()

@app.get("/")
def root():
    #confirms the API is running 
    return {"message": "Bank API is running"}


@app.get("/transactions")
def get_transactions():
    #database connection
    conn = get_conn()
    cursor = conn.cursor()
    #fetch the 50 most recent audit events 
    cursor.execute("""
        SELECT TOP 50 
            CustomerAuditID,
            LoginID,
            CAST(EventTime AS DATETIME) AS EventTime,
            Action,
            IPAddress
        FROM dbo.CustomerAudit 
        ORDER BY CustomerAuditID DESC
    """)
    #extraction of column names from cursor metadata 
    columns = [col[0] for col in cursor.description]
    #Zip column names with row values to create a list fo dicts 
    rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    conn.close()
    return rows 

@app.get("/suspicious")
def get_suspicious():
    #fetch ip with 5+ login failures within 5 min 
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""SELECT IPAddress, CAST(EventTime as DATETIME) AS EventTime, fails_5min 
    FROM dbo.v_FailureBursts
    ORDER BY fails_5min DESC
    """)
      #extraction of column names from cursor metadata 
    columns = [col[0] for col in cursor.description]
    #Zip column names with row values to create a list fo dicts 
    rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return rows

@app.get("/anomalies")
def get_anomalies():
    #fetch to long or to short sessions
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""SELECT LoginID, CAST(LoginTime as DATETIME) AS LoginTime,
    CAST(LogoutTime as DATETIME) AS LogoutTime,
    session_seconds, anomaly_type
    FROM dbo.v_SessionAnomalies
    """)
    #extraction of column names from cursor metadata 
    columns = [col[0] for col in cursor.description]
    #Zip column names with row values to create a list fo dicts 
    rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return rows