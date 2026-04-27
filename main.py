from fastapi import FastAPI
from database_connect import get_conn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bank API is running"}