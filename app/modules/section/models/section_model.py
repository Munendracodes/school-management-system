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


class Section(BaseModel):

    __tablename__ = "sections"

    classroom_id: Mapped[str] = mapped_column(
        ForeignKey("classrooms.id"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    classroom = relationship(
        "Classroom",
        back_populates="sections",
    )

    students: Mapped[List["Student"]] = relationship(
        "Student",
        back_populates="section",
    )

    teacher_mappings: Mapped[List["TeacherSectionMap"]] = relationship(
        "TeacherSectionMap",
        back_populates="section",
    )