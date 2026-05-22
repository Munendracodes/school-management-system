from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.classroom.models.classroom_model import ClassRoom


class ClassRoomRepository:

    @staticmethod
    def create(
        db: Session,
        classroom: ClassRoom,
    ):
        db.add(classroom)
        db.commit()
        db.refresh(classroom)

        return classroom

    @staticmethod
    def get_by_name_and_academic_year(
        db: Session,
        name: str,
        academic_year_id: str,
    ):
        query = select(ClassRoom).where(
            ClassRoom.name == name,
            ClassRoom.academic_year_id == academic_year_id,
            ClassRoom.is_deleted == False,
        )

        return db.scalar(query)

    @staticmethod
    def get_all(
        db: Session,
    ):
        query = select(ClassRoom).where(
            ClassRoom.is_deleted == False,
        )

        return db.scalars(query).all()
    
    @staticmethod
    def get_by_id(
        db: Session,
        classroom_id: str,
    ):
        query = select(ClassRoom).where(
            ClassRoom.id == classroom_id,
            ClassRoom.is_deleted == False,
        )

        return db.scalar(query)