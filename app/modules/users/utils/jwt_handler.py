from datetime import datetime, timedelta, UTC
from typing import Any, Dict

from jose import JWTError, jwt

from app.core.config.settings import settings


ALGORITHM = "HS256"


def create_access_token(
    data: Dict[str, Any],
    expires_minutes: int = 60
) -> str:
    """
    Generate JWT access token
    """

    to_encode = data.copy()

    expire = datetime.now(UTC) + timedelta(
        minutes=expires_minutes
    )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        settings.JWT_SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


def verify_access_token(token: str) -> Dict[str, Any]:
    """
    Verify and decode JWT token
    """

    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:
        raise ValueError("Invalid or expired token")