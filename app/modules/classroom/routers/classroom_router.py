from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.modules.classroom.schemas.classroom_create_schema import (
    ClassRoomCreateSchema,
)
from app.modules.classroom.schemas.classroom_response_schema import (
    ClassRoomResponseSchema,
)
from app.modules.classroom.services.classroom_service import (
    ClassRoomService,
)

from app.modules.users.dependencies.current_user import (
    get_current_user,
)

from app.modules.users.models.user_model import (
    UserModel,
)

router = APIRouter(
    prefix="/classrooms",
    tags=["🏫 Academic Structure"]
)


@router.post(
    "",
    response_model=ClassRoomResponseSchema,
)
def create_classroom(
    payload: ClassRoomCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    return ClassRoomService.create_classroom(
        db=db,
        payload=payload,
    )


@router.get(
    "",
    response_model=list[ClassRoomResponseSchema],
)
def get_all_classrooms(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    return ClassRoomService.get_all_classrooms(
        db=db,
    )