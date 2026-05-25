from uuid import UUID

from sqlalchemy import (
    select,
)

from sqlalchemy.orm import (
    Session,
)

from app.modules.homepage.models.homepage_item_model import (
    HomepageItem,
)


class HomepageItemRepository:

    @staticmethod
    def create(
        db: Session,
        payload: dict,
    ):

        item = HomepageItem(
            **payload
        )

        db.add(
            item
        )

        db.commit()

        db.refresh(
            item
        )

        return item


    @staticmethod
    def get_all(
        db: Session,
    ):

        query = (
            select(
                HomepageItem
            )
            .where(
                HomepageItem.is_deleted.is_(
                    False
                )
            )
            .order_by(
                HomepageItem.display_order
            )
        )

        return db.scalars(
            query
        ).all()


    @staticmethod
    def get_by_id(
        db: Session,
        item_id: UUID,
    ):

        query = (
            select(
                HomepageItem
            )
            .where(
                HomepageItem.id == item_id,
                HomepageItem.is_deleted.is_(
                    False
                )
            )
        )

        return db.scalar(
            query
        )


    @staticmethod
    def get_items(
        db: Session,
        section_id: UUID,
        role: str,
    ):

        query = (
            select(
                HomepageItem
            )
            .where(
                HomepageItem.section_id == section_id,
                HomepageItem.is_active.is_(
                    True
                ),
                HomepageItem.is_deleted.is_(
                    False
                ),
                HomepageItem.visibility_roles.contains(
                    [role]
                )
            )
            .order_by(
                HomepageItem.display_order
            )
        )

        return db.scalars(
            query
        ).all()


    @staticmethod
    def update(
        db: Session,
        item: HomepageItem,
        payload: dict,
    ):

        for key, value in payload.items():

            setattr(
                item,
                key,
                value,
            )

        db.commit()

        db.refresh(
            item
        )

        return item


    @staticmethod
    def soft_delete(
        db: Session,
        item: HomepageItem,
    ):

        item.is_deleted = True

        db.commit()