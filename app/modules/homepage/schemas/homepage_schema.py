from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class HomepageItemResponse(BaseModel):

    id: UUID
    title: str
    subtitle: Optional[str]
    item_type: str
    icon: Optional[str]
    image_url: Optional[str]
    redirect_url: Optional[str]
    config_json: dict

    class Config:
        from_attributes = True


class HomepageSectionResponse(BaseModel):

    id: UUID
    title: str
    description: Optional[str]
    section_type: str
    display_order: int
    config_json: dict

    items: list[HomepageItemResponse]

    class Config:
        from_attributes = True