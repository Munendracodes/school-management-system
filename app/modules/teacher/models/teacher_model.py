from __future__ import annotations

from typing import List

from sqlalchemy import (
    String,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import BaseModel
from app.modules.attendance.models.attendance_model import Attendance
from app.modules.teacher_section_map.models.teacher_section_map_model import TeacherSectionMap


class Teacher(BaseModel):

    __tablename__ = "teachers"

    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    mobile_number: Mapped[str] = mapped_column(
        String(15),
        unique=True,
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(100),
        nullable=True,
    )

    section_mappings: Mapped[List["TeacherSectionMap"]] = relationship(
        "TeacherSectionMap",
        back_populates="teacher",
        cascade="all, delete-orphan",
    )

    attendance_records: Mapped[List["Attendance"]] = relationship(
        "Attendance",
        back_populates="teacher",
        cascade="all, delete-orphan",
    )