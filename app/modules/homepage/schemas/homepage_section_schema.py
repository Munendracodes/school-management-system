from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class HomepageSectionCreateSchema(BaseModel):

    title: str
    description: Optional[str] = None
    section_type: str
    display_order: int = 1
    visibility_roles: list[str]
    background_color: Optional[str] = None
    text_color: Optional[str] = None
    banner_image_url: Optional[str] = None
    config_json: dict = {}


class HomepageSectionUpdateSchema(BaseModel):

    title: Optional[str] = None
    description: Optional[str] = None
    section_type: Optional[str] = None
    display_order: Optional[int] = None
    visibility_roles: Optional[list[str]] = None
    background_color: Optional[str] = None
    text_color: Optional[str] = None
    banner_image_url: Optional[str] = None
    config_json: Optional[dict] = None
    is_active: Optional[bool] = None


class HomepageSectionResponseSchema(
    HomepageSectionCreateSchema
):

    id: UUID

    class Config:
        from_attributes=True