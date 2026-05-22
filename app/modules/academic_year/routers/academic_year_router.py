from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.modules.academic_year.schemas.academic_year_create_schema import (
    AcademicYearCreateSchema,
)
from app.modules.academic_year.schemas.academic_year_response_schema import (
    AcademicYearResponseSchema,
)
from app.modules.academic_year.services.academic_year_service import (
    AcademicYearService,
)

router = APIRouter(
    prefix="/academic-years",
    tags=["Academic Years"],
)


@router.post(
    "",
    response_model=AcademicYearResponseSchema,
)
def create_academic_year(
    payload: AcademicYearCreateSchema,
    db: Session = Depends(get_db),
):
    return AcademicYearService.create_academic_year(
        db=db,
        payload=payload,
    )


@router.get(
    "",
    response_model=list[AcademicYearResponseSchema],
)
def get_all_academic_years(
    db: Session = Depends(get_db),
):
    return AcademicYearService.get_all_academic_years(
        db=db,
    )