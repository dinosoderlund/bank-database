import pypyodbc as odbc

DRIVER = "ODBC Driver 17 for SQL Server"
SERVER = "host.docker.internal,1433"
DATABASE = "Bank_databas"

CONN_STR = (
    f"DRIVER={{{DRIVER}}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "UID=bankuser;"
    "PWD=BankPass123!;"
    "Encrypt=no;"
)

def get_conn():
    return odbc.connect(CONN_STR)