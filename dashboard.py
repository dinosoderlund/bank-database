import streamlit as st 
import pandas as pd 
from database_connect import get_conn

st.title("Bank Dashboard")
#connection
conn = get_conn()

df = pd.read_sql("SELECT TOP 50 * FROM dbo.CustomerAudit ORDER BY CustomerAuditID DESC;", conn)

st.dataframe(df)

#event graph 
st.subheader("Events by Action")
df_actions = pd.read_sql("""
    SELECT Action, COUNT(*) as Count
    FROM dbo.CustomerAudit
    GROUP BY Action
""", conn)
st.bar_chart(df_actions.set_index("Action"))

#fraud indication
st.subheader("⚠️ Suspicious Users")
df_fraud = pd.read_sql("""
    SELECT LoginID, COUNT(*) as FailedLogins
    FROM dbo.CustomerAudit
    WHERE Action = 'LOGIN_FAILURE'
    GROUP BY LoginID
    HAVING COUNT(*) > 10
    ORDER BY FailedLogins DESC
""", conn)

if df_fraud.empty:
    st.succcess("No suspicous activity detected")
else:
    st.warning(f"{len(df_fraud)} user(s) flagged!")
    st.dataframe(df_fraud)


conn.close()