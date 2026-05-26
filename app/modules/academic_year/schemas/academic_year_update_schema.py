from datetime import date
from typing import Optional

from pydantic import BaseModel


class AcademicYearUpdateSchema(BaseModel):

    name: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    is_active: Optional[bool] = None