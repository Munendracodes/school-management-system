from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.dashboard.schemas.dashboard_schema import (
    AdminSummarySchema,
    AttendanceSummarySchema,
    TeacherDashboardSchema,
)

from app.modules.dashboard.services.dashboard_service import (
    DashboardService,
)

router = APIRouter(
    prefix="/dashboard",
    tags=["📊 Dashboard"]
)


@router.get(
    "/admin/summary",
    response_model=AdminSummarySchema,
)
def get_admin_summary(
    db: Session = Depends(get_db),
):
    return DashboardService.get_admin_summary(
        db,
    )


@router.get(
    "/admin/attendance",
    response_model=AttendanceSummarySchema,
)
def get_attendance_summary(
    db: Session = Depends(get_db),
):
    return DashboardService.get_attendance_summary(
        db,
    )


@router.get(
    "/teacher/{teacher_id}",
    response_model=TeacherDashboardSchema,
)
def get_teacher_dashboard(
    teacher_id: UUID,
    db: Session = Depends(get_db),
):
    return DashboardService.get_teacher_dashboard(
        db,
        teacher_id,
    )