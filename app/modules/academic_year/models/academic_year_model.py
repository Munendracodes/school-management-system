from datetime import date

from sqlalchemy import Boolean, Date
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import BaseModel


class AcademicYear(BaseModel):
    __tablename__ = "academic_years"

    name: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
    )

    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    end_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )