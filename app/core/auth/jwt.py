from datetime import datetime, timedelta, timezone
from jose import jwt

from app.core.config.settings import settings


class JWTService:

    @staticmethod
    def create_access_token(data: dict):
        to_encode = data.copy()

        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

        to_encode.update({"exp": expire})

        return jwt.encode(
            to_encode,
            settings.JWT_SECRET_KEY,
            algorithm=settings.JWT_ALGORITHM,
        )
