from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class HomepageItemCreateSchema(
    BaseModel
):

    section_id: UUID

    title: str

    item_type: str

    icon: Optional[str]=None

    redirect_url: Optional[str]=None

    display_order:int=1

    visibility_roles:list[str]

    config_json:dict={}


class HomepageItemUpdateSchema(
    BaseModel
):

    title: Optional[str]=None

    item_type: Optional[str]=None

    icon: Optional[str]=None

    redirect_url: Optional[str]=None

    display_order: Optional[int]=None

    visibility_roles: Optional[
        list[str]
    ]=None

    config_json: Optional[
        dict
    ]=None

    is_active: Optional[
        bool
    ]=None


class HomepageItemResponseSchema(
    HomepageItemCreateSchema
):

    id: UUID

    class Config:

        from_attributes=True