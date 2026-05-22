from sqlalchemy import (
    String,
    Integer,
    Boolean,
    JSON,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.database.base import BaseModel


class HomepageWidget(BaseModel):

    __tablename__ = "homepage_widgets"

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    widget_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    subtitle: Mapped[str] = mapped_column(
        String(500),
        nullable=True,
    )

    image_url: Mapped[str] = mapped_column(
        String(1000),
        nullable=True,
    )

    redirect_url: Mapped[str] = mapped_column(
        String(1000),
        nullable=True,
    )

    sequence: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    visibility_roles: Mapped[list] = mapped_column(
        JSON,
        nullable=False,
    )

    config_json: Mapped[dict] = mapped_column(
        JSON,
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )