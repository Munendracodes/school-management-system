from datetime import date

from pydantic import BaseModel


class AcademicYearCreateSchema(BaseModel):

    name: str
    start_date: date
    end_date: date
    is_active: bool = True