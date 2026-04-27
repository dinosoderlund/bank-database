import streamlit as st 
import pandas as pd 
from database_connect import get_conn

st.title("Bank Dashboard")

conn = get_conn()

# Latest events
df = pd.read_sql("""
    SELECT TOP 50 
        CustomerAuditID,
        LoginID,
        CAST(EventTime AS DATETIME) AS EventTime,
        Action,
        IPAddress
    FROM dbo.CustomerAudit 
    ORDER BY CustomerAuditID DESC
""", conn)
st.dataframe(df)

# Event graph 
st.subheader("Events by Action")
df_actions = pd.read_sql("""
    SELECT Action as action, COUNT(*) as count
    FROM dbo.CustomerAudit
    GROUP BY Action
""", conn)
st.bar_chart(df_actions.set_index("action"))

# Fraud indication
st.subheader("⚠️ Suspicious Activity")
df_fraud = pd.read_sql("""
    SELECT IPAddress, CAST(EventTime AS DATETIME) AS EventTime, fails_5min
    FROM dbo.v_FailureBursts
    ORDER BY fails_5min DESC
""", conn)

if df_fraud.empty:
    st.success("No suspicious activity detected")
else:
    st.warning(f"{len(df_fraud)} suspicious IP(s) flagged!")
    st.dataframe(df_fraud)

conn.close()