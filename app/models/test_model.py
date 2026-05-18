from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base_model import BaseModel


class TestTable(BaseModel):

    __tablename__ = "test_table"

    name: Mapped[str] = mapped_column(String)