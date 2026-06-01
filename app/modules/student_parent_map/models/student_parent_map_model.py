from __future__ import annotations

from sqlalchemy import (
    String,
    ForeignKey,
    UniqueConstraint,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import BaseModel


class StudentParentMap(BaseModel):

    __tablename__ = "student_parent_mappings"

    __table_args__ = (
        UniqueConstraint(
            "student_id",
            "parent_id",
            name="uq_student_parent",
        ),
        UniqueConstraint(
            "student_id",
            "relationship_type",
            name="uq_student_relationship_type",
        ),
    )

    student_id: Mapped[str] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
    )

    parent_id: Mapped[str] = mapped_column(
        ForeignKey("parents.id"),
        nullable=False,
    )

    relationship_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    student = relationship(
        "Student",
        back_populates="parent_mappings",
    )

    parent = relationship(
        "Parent",
        back_populates="student_mappings",
    )