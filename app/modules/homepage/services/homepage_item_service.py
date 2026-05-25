from fastapi import (
    HTTPException,
)

from sqlalchemy.orm import (
    Session,
)

from app.modules.homepage.repositories.homepage_item_repository import (
    HomepageItemRepository,
)

from app.modules.homepage.repositories.homepage_section_repository import (
    HomepageSectionRepository,
)

from app.modules.homepage.schemas.homepage_item_schema import (
    HomepageItemCreateSchema,
    HomepageItemUpdateSchema,
)


class HomepageItemService:

    @staticmethod
    def create(
        db: Session,
        payload: HomepageItemCreateSchema,
    ):

        section = (
            HomepageSectionRepository.get_by_id(
                db=db,
                section_id=payload.section_id,
            )
        )

        if not section:

            raise HTTPException(
                status_code=404,
                detail="Homepage section not found",
            )

        return HomepageItemRepository.create(
            db=db,
            payload=payload.model_dump(),
        )


    @staticmethod
    def get_all(
        db: Session,
    ):

        return HomepageItemRepository.get_all(
            db=db,
        )


    @staticmethod
    def update(
        db: Session,
        item_id,
        payload: HomepageItemUpdateSchema,
    ):

        item = (
            HomepageItemRepository.get_by_id(
                db=db,
                item_id=item_id,
            )
        )

        if not item:

            raise HTTPException(
                status_code=404,
                detail="Homepage item not found",
            )

        update_data = payload.model_dump(
            exclude_unset=True,
            exclude_none=True,
        )

        return HomepageItemRepository.update(
            db=db,
            item=item,
            payload=update_data,
        )


    @staticmethod
    def delete(
        db: Session,
        item_id,
    ):

        item = (
            HomepageItemRepository.get_by_id(
                db=db,
                item_id=item_id,
            )
        )

        if not item:

            raise HTTPException(
                status_code=404,
                detail="Homepage item not found",
            )

        HomepageItemRepository.soft_delete(
            db=db,
            item=item,
        )

        return {
            "message":
            "Homepage item deleted successfully"
        }