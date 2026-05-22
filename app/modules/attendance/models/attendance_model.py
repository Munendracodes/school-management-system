from datetime import date
from sqlalchemy import Index

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

    section_id: Mapped[str] = mapped_column(
        ForeignKey("sections.id"),
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

    student = relationship("Student")

    section = relationship("Section")

    teacher = relationship("Teacher")

    __table_args__ = (
    Index(
        "idx_attendance_date",
        "attendance_date",
    ),
    Index(
        "idx_attendance_student",
        "student_id",
    ),
    Index(
        "idx_attendance_section",
        "section_id",
    ),
)