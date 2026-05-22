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


class StudentParentMapping(BaseModel):

    __tablename__ = "student_parent_mappings"

    student_id: Mapped[str] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
    )

    parent_id: Mapped[str] = mapped_column(
        ForeignKey("parents.id"),
        nullable=False,
    )

    relationship_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    student = relationship("Student")

    parent = relationship(
        "Parent",
        back_populates="students",
    )