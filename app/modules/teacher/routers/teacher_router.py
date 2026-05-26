from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.teacher.schemas.teacher_schema import (
    TeacherCreateSchema,
    TeacherUpdateSchema,
    TeacherResponseSchema,
    TeacherSectionMappingCreateSchema,
    TeacherSectionMappingResponseSchema,
)

from app.modules.teacher.services.teacher_service import (
    TeacherService,
)

from app.modules.users.dependencies.current_user import (
    get_current_user,
)

from app.modules.users.models.user_model import (
    UserModel,
)

router = APIRouter(
    prefix="/teachers",
    tags=["👨‍🏫 Teacher Management"]
)


@router.post(
    "",
    response_model=TeacherResponseSchema,
)
def create_teacher(
    payload: TeacherCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    return TeacherService.create_teacher(
        db,
        payload,
    )


@router.get(
    "",
    response_model=list[TeacherResponseSchema],
)
def get_teachers(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    return TeacherService.get_teachers(db)


@router.get(
    "/{teacher_id}",
    response_model=TeacherResponseSchema,
)
def get_teacher_by_id(
    teacher_id: UUID,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    return TeacherService.get_teacher_by_id(
        db,
        teacher_id,
    )


@router.put(
    "/{teacher_id}",
    response_model=TeacherResponseSchema,
)
def update_teacher(
    teacher_id: UUID,
    payload: TeacherUpdateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    return TeacherService.update_teacher(
        db,
        teacher_id,
        payload,
    )


@router.delete("/{teacher_id}")
def delete_teacher(
    teacher_id: UUID,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    return TeacherService.delete_teacher(
        db,
        teacher_id,
    )


@router.post(
    "/map-section",
    response_model=TeacherSectionMappingResponseSchema,
)
def map_teacher_section(
    payload: TeacherSectionMappingCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    return TeacherService.map_teacher_section(
        db,
        payload,
    )