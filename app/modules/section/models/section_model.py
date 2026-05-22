from sqlalchemy import (
    String,
    Boolean,
    Integer,
    ForeignKey,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import BaseModel


class Section(BaseModel):

    __tablename__ = "sections"

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    classroom_id: Mapped[str] = mapped_column(
        ForeignKey("classrooms.id"),
        nullable=False,
    )

    capacity: Mapped[int] = mapped_column(
        Integer,
        default=40,
    )

    display_order: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    classroom = relationship("ClassRoom")