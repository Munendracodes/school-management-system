from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import BaseModel


class ClassRoom(BaseModel):
    __tablename__ = "classrooms"

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    display_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    academic_year_id: Mapped[str] = mapped_column(
        ForeignKey("academic_years.id"),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )