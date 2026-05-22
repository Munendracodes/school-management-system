from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.section.models.section_model import Section


class SectionRepository:

    @staticmethod
    def create(
        db: Session,
        payload: dict,
    ):
        section = Section(**payload)

        db.add(section)

        db.commit()
        db.refresh(section)

        return section

    @staticmethod
    def get_all(
        db: Session,
    ):
        query = select(Section).where(
            Section.is_deleted == False,
        )

        return db.scalars(query).all()

    @staticmethod
    def get_by_id(
        db: Session,
        section_id: str,
    ):
        query = select(Section).where(
            Section.id == section_id,
            Section.is_deleted == False,
        )

        return db.scalar(query)

    @staticmethod
    def update(
        db: Session,
        section: Section,
        payload: dict,
    ):
        for key, value in payload.items():
            setattr(section, key, value)

        db.commit()
        db.refresh(section)

        return section

    @staticmethod
    def soft_delete(
        db: Session,
        section: Section,
    ):
        section.is_deleted = True

        db.commit()