from datetime import date

from sqlalchemy import (
    String,
    Boolean,
    Date,
    ForeignKey,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import BaseModel


class Student(BaseModel):

    __tablename__ = "students"

    admission_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    full_name: Mapped[str] = mapped_column(
        String(150),
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

    mobile_number: Mapped[str] = mapped_column(
        String(20),
        nullable=True,
    )

    email: Mapped[str] = mapped_column(
        String(150),
        nullable=True,
    )

    address: Mapped[str] = mapped_column(
        String(500),
        nullable=True,
    )

    guardian_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    guardian_mobile_number: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    academic_year_id: Mapped[str] = mapped_column(
        ForeignKey("academic_years.id"),
        nullable=False,
    )

    classroom_id: Mapped[str] = mapped_column(
        ForeignKey("classrooms.id"),
        nullable=False,
    )

    section_id: Mapped[str] = mapped_column(
        ForeignKey("sections.id"),
        nullable=False,
    )

    roll_number: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    admission_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    academic_year = relationship("AcademicYear")
    classroom = relationship("ClassRoom")
    section = relationship("Section")