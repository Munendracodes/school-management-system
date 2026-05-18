import time

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

max_retries = 10
retry_delay = 3

for attempt in range(max_retries):
    try:
        connection = engine.connect()
        print("Database connected successfully")
        break
    except OperationalError:
        print(f"Database not ready... retrying ({attempt + 1}/{max_retries})")
        time.sleep(retry_delay)
else:
    raise Exception("Could not connect to PostgreSQL")