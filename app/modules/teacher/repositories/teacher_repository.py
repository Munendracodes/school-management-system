from sqlalchemy import (
    func,
    select,
)

from sqlalchemy.orm import Session

from app.modules.teacher.models.teacher_model import (
    Teacher,
)

from app.modules.teacher_section_map.models.teacher_section_map_model import (
    TeacherSectionMap,
)


class TeacherRepository:

    @staticmethod
    def create(
        db: Session,
        payload: dict,
    ):
        teacher = Teacher(**payload)

        db.add(teacher)

        db.commit()
        db.refresh(teacher)

        return teacher

    @staticmethod
    def get_all(
        db: Session,
    ):
        query = (
            select(Teacher)
            .where(
                Teacher.is_deleted.is_(False)
            )
        )

        return db.scalars(query).all()

    @staticmethod
    def get_by_id(
        db: Session,
        teacher_id: str,
    ):
        query = (
            select(Teacher)
            .where(
                Teacher.id == teacher_id,
                Teacher.is_deleted.is_(False),
            )
        )

        return db.scalar(query)

    @staticmethod
    def get_by_mobile_number(
        db: Session,
        mobile_number: str,
    ):
        query = (
            select(Teacher)
            .where(
                Teacher.mobile_number == mobile_number,
                Teacher.is_deleted.is_(False),
            )
        )

        return db.scalar(query)

    @staticmethod
    def update(
        db: Session,
        teacher: Teacher,
        payload: dict,
    ):
        for key, value in payload.items():
            setattr(
                teacher,
                key,
                value,
            )

        db.commit()
        db.refresh(teacher)

        return teacher

    @staticmethod
    def soft_delete(
        db: Session,
        teacher: Teacher,
    ):
        teacher.is_deleted = True

        db.commit()

    @staticmethod
    def get_count(
        db: Session,
    ):

        query = (
            select(
                func.count(
                    Teacher.id
                )
            )
            .where(
                Teacher.is_deleted.is_(False)
            )
        )

        return db.scalar(query) or 0
    
    @staticmethod
    def create_teacher_section_mapping(
        db: Session,
        payload: dict,
    ):

        existing = db.scalar(

            select(
                TeacherSectionMap
            )

            .where(
                TeacherSectionMap.teacher_id ==
                payload["teacher_id"],

                TeacherSectionMap.section_id ==
                payload["section_id"]
            )
        )

        if existing:
            return existing

        mapping = TeacherSectionMap(
            **payload
        )

        db.add(
            mapping
        )

        db.commit()

        db.refresh(
            mapping
        )

        return mapping