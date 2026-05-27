from __future__ import annotations

from typing import List

from sqlalchemy import (
    String,
    ForeignKey,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import BaseModel


class Classroom(BaseModel):

    __tablename__ = "classrooms"

    academic_year_id: Mapped[str] = mapped_column(
        ForeignKey("academic_years.id"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    academic_year = relationship(
        "AcademicYear",
        back_populates="classrooms",
    )

    sections: Mapped[List["Section"]] = relationship(
        "Section",
        back_populates="classroom",
    )