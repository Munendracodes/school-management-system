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
from app.modules.section.models.section_model import Section
from app.modules.academic_year.models.academic_year_model import AcademicYear


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