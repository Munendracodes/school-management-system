from sqlalchemy import (
    String,
    Boolean,
    ForeignKey,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import BaseModel


class TeacherSectionMapping(BaseModel):

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

    is_class_teacher: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    teacher = relationship(
        "Teacher",
        back_populates="sections",
    )

    section = relationship("Section")