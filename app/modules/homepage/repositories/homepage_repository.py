from sqlalchemy import select

from sqlalchemy.orm import Session

from app.modules.homepage.models.homepage_widget_model import (
    HomepageWidget,
)


class HomepageRepository:

    @staticmethod
    def create(
        db: Session,
        payload: dict,
    ):
        widget = HomepageWidget(**payload)

        db.add(widget)

        db.commit()

        db.refresh(widget)

        return widget

    @staticmethod
    def get_all(
        db: Session,
    ):
        query = (
            select(HomepageWidget)
            .where(
                HomepageWidget.is_deleted == False,
            )
            .order_by(
                HomepageWidget.sequence.asc(),
            )
        )

        return db.scalars(query).all()

    @staticmethod
    def get_visible_widgets(
        db: Session,
        role: str,
    ):
        query = (
            select(HomepageWidget)
            .where(
                HomepageWidget.is_active == True,
                HomepageWidget.is_deleted == False,
            )
            .order_by(
                HomepageWidget.sequence.asc(),
            )
        )

        widgets = db.scalars(query).all()

        return [
            widget
            for widget in widgets
            if role in widget.visibility_roles
        ]

    @staticmethod
    def get_by_id(
        db: Session,
        widget_id,
    ):
        query = select(HomepageWidget).where(
            HomepageWidget.id == widget_id,
            HomepageWidget.is_deleted == False,
        )

        return db.scalar(query)

    @staticmethod
    def update(
        db: Session,
        widget,
        payload: dict,
    ):
        for key, value in payload.items():
            setattr(widget, key, value)

        db.commit()

        db.refresh(widget)

        return widget

    @staticmethod
    def soft_delete(
        db: Session,
        widget,
    ):
        widget.is_deleted = True

        db.commit()