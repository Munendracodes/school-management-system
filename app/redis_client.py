import redis
from app.config import REDIS_URL

redis_client = redis.Redis.from_url(REDIS_URL)

redis_client.ping()

print("Redis connected successfully")