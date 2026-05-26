from __future__ import annotations

from datetime import date
from typing import List

from sqlalchemy import (
    String,
    Date,
    Boolean,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import BaseModel


class AcademicYear(BaseModel):

    __tablename__ = "academic_years"

    name: Mapped[str] = mapped_column(
        String(20),
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

    classrooms: Mapped[List["Classroom"]] = relationship(
        "Classroom",
        back_populates="academic_year",
    )