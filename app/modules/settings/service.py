from sqlalchemy.orm import Session

from app.modules.settings.repository import (
    SchoolSettingsRepository,
)

from app.modules.settings.schemas import (
    BootstrapResponse,
    SchoolSettingsCreate,
    SchoolSettingsUpdate,
)


class SchoolSettingsService:

    @staticmethod
    def get_settings(
        db: Session,
    ):
        return (
            SchoolSettingsRepository
            .get_settings(db)
        )

    @staticmethod
    def create_settings(
        db: Session,
        payload: SchoolSettingsCreate,
    ):
        existing_settings = (
            SchoolSettingsRepository
            .get_settings(db)
        )

        if existing_settings:
            raise ValueError(
                "School settings already exist"
            )

        return (
            SchoolSettingsRepository
            .create_settings(
                db,
                payload,
            )
        )

    @staticmethod
    def update_settings(
        db: Session,
        payload: SchoolSettingsUpdate,
    ):
        settings = (
            SchoolSettingsRepository
            .get_settings(db)
        )

        if not settings:
            raise ValueError(
                "School settings not found"
            )

        return (
            SchoolSettingsRepository
            .update_settings(
                db,
                settings,
                payload,
            )
        )

    @staticmethod
    def get_bootstrap_data(
        db: Session,
    ):
        settings = (
            SchoolSettingsRepository
            .get_settings(db)
        )

        if not settings:
            raise ValueError(
                "School settings not found"
            )
        
        return BootstrapResponse(
            school_name=settings.school_name,
            tag_line=settings.tag_line,
            logo_url=settings.logo_url,
            primary_color=settings.primary_color,
            secondary_color=settings.secondary_color,
            welcome_screen=settings.welcome_screen,
            login_screen=settings.login_screen,
        )
    
    @staticmethod
    def delete_settings(
        db: Session,
    ):
        settings = (
            SchoolSettingsRepository
            .get_settings(db)
        )

        if not settings:
            raise ValueError(
                "School settings not found"
            )

        db.delete(settings)

        db.commit()

        return True