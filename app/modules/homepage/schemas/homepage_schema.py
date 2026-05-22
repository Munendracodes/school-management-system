from uuid import UUID
from typing import Optional

from pydantic import BaseModel

from app.modules.homepage.enums.widget_type_enum import (
    WidgetTypeEnum,
)


class HomepageWidgetCreateSchema(BaseModel):

    title: str

    widget_type: WidgetTypeEnum

    subtitle: Optional[str] = None

    image_url: Optional[str] = None

    redirect_url: Optional[str] = None

    sequence: int = 1

    visibility_roles: list[str]

    config_json: Optional[dict] = None

    is_active: bool = True


class HomepageWidgetUpdateSchema(BaseModel):

    title: Optional[str] = None

    subtitle: Optional[str] = None

    image_url: Optional[str] = None

    redirect_url: Optional[str] = None

    sequence: Optional[int] = None

    visibility_roles: Optional[list[str]] = None

    config_json: Optional[dict] = None

    is_active: Optional[bool] = None


class HomepageWidgetResponseSchema(BaseModel):

    id: UUID

    title: str

    widget_type: str

    subtitle: Optional[str]

    image_url: Optional[str]

    redirect_url: Optional[str]

    sequence: int

    visibility_roles: list[str]

    config_json: Optional[dict]

    is_active: bool

    class Config:
        from_attributes = True