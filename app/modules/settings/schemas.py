from uuid import UUID

from pydantic import BaseModel, ConfigDict


class SchoolSettingsBase(BaseModel):
    school_name: str

    school_code: str

    logo_url: str | None = None

    tag_line: str | None = None

    primary_color: str | None = None

    secondary_color: str | None = None

    welcome_screen: dict | None = None

    login_screen: dict | None = None

    features_enabled: dict | None = None


class SchoolSettingsCreate(
    SchoolSettingsBase
):
    pass


class SchoolSettingsUpdate(BaseModel):
    school_name: str | None = None

    school_code: str | None = None

    logo_url: str | None = None

    tag_line: str | None = None

    primary_color: str | None = None

    secondary_color: str | None = None

    welcome_screen: dict | None = None

    login_screen: dict | None = None

    features_enabled: dict | None = None


class SchoolSettingsResponse(
    SchoolSettingsBase
):
    id: UUID

    model_config = ConfigDict(
        from_attributes=True
    )


class BootstrapResponse(BaseModel):
    school_name: str

    tag_line: str | None = None

    logo_url: str | None = None

    primary_color: str | None = None

    secondary_color: str | None = None

    welcome_screen: dict | None = None

    login_screen: dict | None = None