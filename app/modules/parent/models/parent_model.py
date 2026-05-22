from sqlalchemy import (
    String,
    Boolean,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import BaseModel


class Parent(BaseModel):

    __tablename__ = "parents"

    father_name: Mapped[str] = mapped_column(
        String(150),
        nullable=True,
    )

    mother_name: Mapped[str] = mapped_column(
        String(150),
        nullable=True,
    )

    guardian_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    mobile_number: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        unique=True,
    )

    alternate_mobile_number: Mapped[str] = mapped_column(
        String(20),
        nullable=True,
    )

    email: Mapped[str] = mapped_column(
        String(150),
        nullable=True,
    )

    occupation: Mapped[str] = mapped_column(
        String(150),
        nullable=True,
    )

    address: Mapped[str] = mapped_column(
        String(500),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    students = relationship(
        "StudentParentMapping",
        back_populates="parent",
    )