from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.modules.academic_year.repositories.academic_year_repository import (
    AcademicYearRepository,
)
from app.modules.classroom.models.classroom_model import Classroom as ClassRoom
from app.modules.classroom.repositories.classroom_repository import (
    ClassRoomRepository,
)
from app.modules.classroom.schemas.classroom_create_schema import (
    ClassRoomCreateSchema,
)


class ClassRoomService:

    @staticmethod
    def create_classroom(
        db: Session,
        payload: ClassRoomCreateSchema,
    ):

        academic_year = AcademicYearRepository.get_by_id(
            db=db,
            academic_year_id=str(payload.academic_year_id),
        )

        if not academic_year:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Academic year not found",
            )

        existing_classroom = (
            ClassRoomRepository.get_by_name_and_academic_year(
                db=db,
                name=payload.name,
                academic_year_id=str(payload.academic_year_id),
            )
        )

        if existing_classroom:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Class already exists in this academic year",
            )

        classroom = ClassRoom(
            name=payload.name,
            academic_year_id=str(payload.academic_year_id)
        )

        return ClassRoomRepository.create(
            db=db,
            classroom=classroom,
        )

    @staticmethod
    def get_all_classrooms(
        db: Session,
    ):
        return ClassRoomRepository.get_all(db=db)