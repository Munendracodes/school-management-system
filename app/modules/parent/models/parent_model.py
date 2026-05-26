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
from app.modules.student_parent_map.models.student_parent_map_model import StudentParentMap


class Parent(BaseModel):

    __tablename__ = "parents"

    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    mobile_number: Mapped[str] = mapped_column(
        String(15),
        nullable=False,
        unique=True,
    )

    email: Mapped[str] = mapped_column(
        String(100),
        nullable=True,
    )

    student_mappings: Mapped[List["StudentParentMap"]] = relationship(
        "StudentParentMap",
        back_populates="parent",
        cascade="all, delete-orphan",
    )