import streamlit as st 
import pandas as pd 
from database_connect import get_conn

st.title("Bank Dashboard")

conn = get_conn()

df = pd.read_sql("SELECT TOP 50 * FROM dbo.CustomerAudit ORDER BY CustomerAuditID DESC;", conn)

st.dataframe(df)

conn.close()