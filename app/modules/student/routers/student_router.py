from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.student.schemas.student_schema import (
    StudentCreateSchema,
    StudentUpdateSchema,
    StudentResponseSchema,
)

from app.modules.student.services.student_service import (
    StudentService,
)

from app.modules.users.dependencies.current_user import (
    get_current_user,
)

from app.modules.users.models.user_model import (
    UserModel,
)

router = APIRouter(
    prefix="/students",
    tags=["🎓 Student Management"]
)


@router.post(
    "",
    response_model=StudentResponseSchema,
)
def create_student(
    payload: StudentCreateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(
        get_current_user
    )
):
    return StudentService.create_student(
        db,
        payload,
    )


@router.get(
    "",
    response_model=list[StudentResponseSchema],
)
def get_students(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(
        get_current_user
    )
):
    return StudentService.get_students(db)


@router.get(
    "/{student_id}",
    response_model=StudentResponseSchema,
)
def get_student_by_id(
    student_id: UUID,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(
        get_current_user
    )
):
    return StudentService.get_student_by_id(
        db,
        student_id,
    )


@router.put(
    "/{student_id}",
    response_model=StudentResponseSchema,
)
def update_student(
    student_id: UUID,
    payload: StudentUpdateSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(
        get_current_user
    )
):
    return StudentService.update_student(
        db,
        student_id,
        payload,
    )


@router.delete("/{student_id}")
def delete_student(
    student_id: UUID,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(
        get_current_user
    )
):
    return StudentService.delete_student(
        db,
        student_id,
    )