from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.attendance.schemas.attendance_schema import (
    AttendanceCreateSchema,
    AttendanceUpdateSchema,
    AttendanceResponseSchema,
)

from app.modules.attendance.services.attendance_service import (
    AttendanceService,
)

router = APIRouter(
    prefix="/attendance",
    tags=["📝 Attendance"]
)


@router.post(
    "",
    response_model=AttendanceResponseSchema,
)
def create_attendance(
    payload: AttendanceCreateSchema,
    db: Session = Depends(get_db),
):
    return AttendanceService.create_attendance(
        db,
        payload,
    )


@router.get(
    "",
    response_model=list[AttendanceResponseSchema],
)
def get_attendance(
    db: Session = Depends(get_db),
):
    return AttendanceService.get_attendance(db)


@router.get(
    "/student/{student_id}",
    response_model=list[AttendanceResponseSchema],
)
def get_attendance_by_student(
    student_id: UUID,
    db: Session = Depends(get_db),
):
    return AttendanceService.get_attendance_by_student(
        db,
        student_id,
    )


@router.get(
    "/section/{section_id}",
    response_model=list[AttendanceResponseSchema],
)
def get_attendance_by_section(
    section_id: UUID,
    db: Session = Depends(get_db),
):
    return AttendanceService.get_attendance_by_section(
        db,
        section_id,
    )


@router.put(
    "/{attendance_id}",
    response_model=AttendanceResponseSchema,
)
def update_attendance(
    attendance_id: UUID,
    payload: AttendanceUpdateSchema,
    db: Session = Depends(get_db),
):
    return AttendanceService.update_attendance(
        db,
        attendance_id,
        payload,
    )


@router.delete("/{attendance_id}")
def delete_attendance(
    attendance_id: UUID,
    db: Session = Depends(get_db),
):
    return AttendanceService.delete_attendance(
        db,
        attendance_id,
    )