from __future__ import annotations

from datetime import date
from typing import List

from sqlalchemy import (
    String,
    Date,
    ForeignKey,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import BaseModel
from app.modules.attendance.models.attendance_model import Attendance
from app.modules.student_parent_map.models.student_parent_map_model import StudentParentMap


class Student(BaseModel):

    __tablename__ = "students"

    admission_number: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
    )

    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    gender: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    date_of_birth: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    section_id: Mapped[str] = mapped_column(
        ForeignKey("sections.id"),
        nullable=False,
    )

    section = relationship(
        "Section",
        back_populates="students",
    )

    parent_mappings: Mapped[List["StudentParentMap"]] = relationship(
    "StudentParentMap",
    back_populates="student",
    cascade="all, delete-orphan",
    )

    attendance_records = relationship(
        "Attendance",
        back_populates="student",
        cascade="all, delete-orphan",
    )