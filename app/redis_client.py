import redis
from app.configs.settings import settings
from app.core.logger import logger

redis_client = redis.Redis.from_url(settings.REDIS_URL)

redis_client.ping()

logger.info("Redis connected successfully")