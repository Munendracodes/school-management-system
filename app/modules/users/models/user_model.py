from sqlalchemy import (
    Boolean,
    ForeignKey,
    String,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import BaseModel


class UserModel(BaseModel):
    __tablename__ = "users"

    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    mobile_number: Mapped[str] = mapped_column(
        String(15),
        unique=True,
        nullable=False,
        index=True
    )

    email: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        nullable=True
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    role_id: Mapped[str] = mapped_column(
        ForeignKey("roles.id"),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    is_first_login: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    created_by: Mapped[str | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    role = relationship(
        "RoleModel",
        back_populates="users"
    )