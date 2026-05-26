from __future__ import annotations

from datetime import date

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


class Attendance(BaseModel):

    __tablename__ = "attendance_records"

    student_id: Mapped[str] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
    )

    teacher_id: Mapped[str] = mapped_column(
        ForeignKey("teachers.id"),
        nullable=False,
    )

    attendance_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    remarks: Mapped[str] = mapped_column(
        String(500),
        nullable=True,
    )

    student = relationship(
        "Student",
        back_populates="attendance_records",
    )

    teacher = relationship(
        "Teacher",
        back_populates="attendance_records",
    )