from sqlalchemy.orm import Session

from app.modules.settings.models import (
    SchoolSettings,
)

from app.modules.settings.schemas import (
    SchoolSettingsCreate,
    SchoolSettingsUpdate,
)


class SchoolSettingsRepository:

    @staticmethod
    def get_settings(
        db: Session,
    ):
        return (
            db.query(SchoolSettings)
            .first()
        )

    @staticmethod
    def create_settings(
        db: Session,
        payload: SchoolSettingsCreate,
    ):
        settings = SchoolSettings(
            **payload.model_dump()
        )

        db.add(settings)

        db.commit()

        db.refresh(settings)

        return settings

    @staticmethod
    def update_settings(
        db: Session,
        settings: SchoolSettings,
        payload: SchoolSettingsUpdate,
    ):
        update_data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in (
            update_data.items()
        ):
            setattr(
                settings,
                key,
                value,
            )

        db.commit()

        db.refresh(settings)

        return settings