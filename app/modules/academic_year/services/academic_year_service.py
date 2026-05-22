from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.modules.academic_year.models.academic_year_model import AcademicYear
from app.modules.academic_year.repositories.academic_year_repository import (
    AcademicYearRepository,
)
from app.modules.academic_year.schemas.academic_year_create_schema import (
    AcademicYearCreateSchema,
)


class AcademicYearService:

    @staticmethod
    def create_academic_year(
        db: Session,
        payload: AcademicYearCreateSchema,
    ):

        if payload.start_date >= payload.end_date:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Start date must be less than end date",
            )

        existing_year = AcademicYearRepository.get_by_name(
            db=db,
            name=payload.name,
        )

        if existing_year:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Academic year already exists",
            )

        if payload.is_active:
            AcademicYearRepository.deactivate_all(db=db)

        academic_year = AcademicYear(
            name=payload.name,
            start_date=payload.start_date,
            end_date=payload.end_date,
            is_active=payload.is_active,
        )

        return AcademicYearRepository.create(
            db=db,
            academic_year=academic_year,
        )

    @staticmethod
    def get_all_academic_years(
        db: Session,
    ):
        return AcademicYearRepository.get_all(db=db)