from __future__ import annotations

from sqlalchemy import (
    String,
    ForeignKey,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from sqlalchemy import UniqueConstraint


from app.database.base import BaseModel


class TeacherSectionMap(BaseModel):

    __tablename__ = "teacher_section_mappings"

    teacher_id: Mapped[str] = mapped_column(
        ForeignKey("teachers.id"),
        nullable=False,
    )

    section_id: Mapped[str] = mapped_column(
        ForeignKey("sections.id"),
        nullable=False,
    )

    subject_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    teacher = relationship(
        "Teacher",
        back_populates="section_mappings",
    )

    section = relationship(
        "Section",
        back_populates="teacher_mappings",
    )

    __table_args__ = (
    UniqueConstraint(
        "teacher_id",
        "section_id",
        "subject_name",
        name="uq_teacher_section_subject"
    ),
)