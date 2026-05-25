from sqlalchemy import (
    String,
    Integer,
    Boolean,
    Text,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from sqlalchemy.dialects.postgresql import (
    JSONB,
)

from app.database.base import BaseModel


class HomepageSection(BaseModel):

    __tablename__ = "homepage_sections"

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    section_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    display_order: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    visibility_roles: Mapped[list] = mapped_column(
        JSONB,
        nullable=False,
        default=list,
    )

    background_color: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    text_color: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    banner_image_url: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    config_json: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
        default=dict,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    items = relationship(
        "HomepageItem",
        back_populates="section",
        cascade="all, delete-orphan",
    )