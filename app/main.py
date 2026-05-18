from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.redis_client import redis_client

app = FastAPI(title="School Management System API")


@app.get("/")
def health(db: Session = Depends(get_db)):

    db.execute(text("SELECT 1"))

    redis_client.ping()

    return {
        "status": "running",
        "database": "connected",
        "redis": "connected"
    }