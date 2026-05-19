from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import BaseModel


class SchoolSettings(BaseModel):
    __tablename__ = "school_settings"

    school_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    school_code: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    logo_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    primary_color: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    secondary_color: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    welcome_screen: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    login_screen: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    features_enabled: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )