from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    full_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )