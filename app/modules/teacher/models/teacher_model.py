from datetime import date

from sqlalchemy import (
    String,
    Boolean,
    Integer,
    Date,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import BaseModel


class Teacher(BaseModel):

    __tablename__ = "teachers"

    employee_id: Mapped[str] = mapped_column(
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

    mobile_number: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(150),
        nullable=True,
    )

    qualification: Mapped[str] = mapped_column(
        String(200),
        nullable=True,
    )

    experience_years: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    joining_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    is_class_teacher: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    sections = relationship(
        "TeacherSectionMapping",
        back_populates="teacher",
    )