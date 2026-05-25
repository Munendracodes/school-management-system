from fastapi import (
    HTTPException,
)

from sqlalchemy.orm import (
    Session,
)

from app.modules.homepage.repositories.homepage_section_repository import (
    HomepageSectionRepository,
)

from app.modules.homepage.schemas.homepage_section_schema import (
    HomepageSectionCreateSchema,
    HomepageSectionUpdateSchema,
)


class HomepageSectionService:

    @staticmethod
    def create(
        db: Session,
        payload: HomepageSectionCreateSchema,
    ):

        return HomepageSectionRepository.create(
            db=db,
            payload=payload.model_dump(),
        )


    @staticmethod
    def get_all(
        db: Session,
    ):

        return HomepageSectionRepository.get_all(
            db=db,
        )


    @staticmethod
    def update(
        db: Session,
        section_id,
        payload: HomepageSectionUpdateSchema,
    ):

        section = (
            HomepageSectionRepository.get_by_id(
                db=db,
                section_id=section_id,
            )
        )

        if not section:

            raise HTTPException(
                status_code=404,
                detail="Homepage section not found",
            )

        update_data = payload.model_dump(
            exclude_unset=True,
            exclude_none=True,
        )

        return HomepageSectionRepository.update(
            db=db,
            section=section,
            payload=update_data,
        )


    @staticmethod
    def delete(
        db: Session,
        section_id,
    ):

        section = (
            HomepageSectionRepository.get_by_id(
                db=db,
                section_id=section_id,
            )
        )

        if not section:

            raise HTTPException(
                status_code=404,
                detail="Homepage section not found",
            )

        HomepageSectionRepository.soft_delete(
            db=db,
            section=section,
        )

        return {
            "message":
            "Homepage section deleted successfully"
        }