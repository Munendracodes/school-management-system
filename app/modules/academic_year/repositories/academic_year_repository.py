from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.academic_year.models.academic_year_model import AcademicYear


class AcademicYearRepository:

    @staticmethod
    def create(
        db: Session,
        academic_year: AcademicYear,
    ) -> AcademicYear:
        db.add(academic_year)
        db.commit()
        db.refresh(academic_year)

        return academic_year

    @staticmethod
    def get_by_name(
        db: Session,
        name: str,
    ):
        query = select(AcademicYear).where(
            AcademicYear.name == name,
            AcademicYear.is_deleted == False,
        )

        return db.scalar(query)

    @staticmethod
    def get_active_year(
        db: Session,
    ):
        query = select(AcademicYear).where(
            AcademicYear.is_active == True,
            AcademicYear.is_deleted == False,
        )

        return db.scalar(query)

    @staticmethod
    def deactivate_all(
        db: Session,
    ):
        query = select(AcademicYear).where(
            AcademicYear.is_active == True,
            AcademicYear.is_deleted == False,
        )

        academic_years = db.scalars(query).all()

        for year in academic_years:
            year.is_active = False

        db.commit()

    @staticmethod
    def get_all(
        db: Session,
    ):
        query = select(AcademicYear).where(
            AcademicYear.is_deleted == False,
        )

        return db.scalars(query).all()
    
    @staticmethod
    def get_by_id(
        db: Session,
        academic_year_id: str,
    ):
        query = select(AcademicYear).where(
            AcademicYear.id == academic_year_id,
            AcademicYear.is_deleted == False,
        )

        return db.scalar(query)