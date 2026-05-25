from uuid import UUID

from sqlalchemy import (
    String,
    Integer,
    Boolean,
    Text,
    ForeignKey,
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


class HomepageItem(BaseModel):

    __tablename__ = "homepage_items"

    section_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            "homepage_sections.id"
        ),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    item_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    icon: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    redirect_url: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    display_order: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    visibility_roles: Mapped[list] = mapped_column(
        JSONB,
        default=list,
    )

    config_json: Mapped[dict] = mapped_column(
        JSONB,
        default=dict,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    section=relationship(
        "HomepageSection",
        back_populates="items"
    )