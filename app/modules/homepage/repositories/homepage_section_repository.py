from uuid import UUID

from sqlalchemy import (
    select,
)

from sqlalchemy.orm import (
    Session,
    selectinload,
)

from app.modules.homepage.models.homepage_section_model import (
    HomepageSection,
)


class HomepageSectionRepository:

    @staticmethod
    def create(
        db: Session,
        payload: dict,
    ):

        section = HomepageSection(
            **payload
        )

        db.add(
            section
        )

        db.commit()

        db.refresh(
            section
        )

        return section


    @staticmethod
    def get_all(
        db: Session,
    ):

        query = (
            select(
                HomepageSection
            )
            .where(
                HomepageSection.is_deleted.is_(
                    False
                )
            )
            .order_by(
                HomepageSection.display_order
            )
        )

        return db.scalars(
            query
        ).all()


    @staticmethod
    def get_by_id(
        db: Session,
        section_id: UUID,
    ):

        query = (
            select(
                HomepageSection
            )
            .where(
                HomepageSection.id == section_id,
                HomepageSection.is_deleted.is_(
                    False
                ),
            )
        )

        return db.scalar(
            query
        )


    @staticmethod
    def get_visible_sections(
        db: Session,
        role: str,
    ):

        query = (
            select(
                HomepageSection
            )
            .options(
                selectinload(
                    HomepageSection.items
                )
            )
            .where(
                HomepageSection.is_active.is_(
                    True
                ),
                HomepageSection.is_deleted.is_(
                    False
                ),
                HomepageSection.visibility_roles.contains(
                    [role]
                )
            )
            .order_by(
                HomepageSection.display_order
            )
        )

        return db.scalars(
            query
        ).all()


    @staticmethod
    def update(
        db: Session,
        section: HomepageSection,
        payload: dict,
    ):

        for key, value in payload.items():

            setattr(
                section,
                key,
                value,
            )

        db.commit()

        db.refresh(
            section
        )

        return section


    @staticmethod
    def soft_delete(
        db: Session,
        section: HomepageSection,
    ):

        section.is_deleted = True

        db.commit()