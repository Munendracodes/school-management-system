from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.parent.schemas.parent_schema import (
    ParentCreateSchema,
    ParentUpdateSchema,
    ParentResponseSchema,
    StudentParentMappingCreateSchema,
    StudentParentMappingResponseSchema,
)

from app.modules.parent.services.parent_service import (
    ParentService,
)

from app.modules.users.dependencies.current_user import (
    get_current_user,
)

from app.modules.users.models.user_model import (
    UserModel,
)

router = APIRouter(
    prefix="/parents",
    tags=["👨‍👩‍👧 Parent Management"]
)


@router.post(
    "",
    response_model=ParentResponseSchema,
)
def create_parent(
    payload: ParentCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    return ParentService.create_parent(
        db,
        payload,
    )


@router.get(
    "",
    response_model=list[ParentResponseSchema],
)
def get_parents(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    return ParentService.get_parents(db)


@router.get(
    "/{parent_id}",
    response_model=ParentResponseSchema,
)
def get_parent_by_id(
    parent_id: UUID,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    return ParentService.get_parent_by_id(
        db,
        parent_id,
    )


@router.put(
    "/{parent_id}",
    response_model=ParentResponseSchema,
)
def update_parent(
    parent_id: UUID,
    payload: ParentUpdateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    return ParentService.update_parent(
        db,
        parent_id,
        payload,
    )


@router.delete("/{parent_id}")
def delete_parent(
    parent_id: UUID,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    return ParentService.delete_parent(
        db,
        parent_id,
    )


@router.post(
    "/map-student",
    response_model=StudentParentMappingResponseSchema,
)
def map_student_parent(
    payload: StudentParentMappingCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    return ParentService.map_student_parent(
        db,
        payload,
    )