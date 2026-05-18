from fastapi import FastAPI #ignore-type

from app.database.db import connection
from app.redis_client import redis_client

app = FastAPI(title="School Management System API")


@app.get("/")
def health():
    return {
        "status": "running",
        "database": "connected",
        "redis": "connected"
    }