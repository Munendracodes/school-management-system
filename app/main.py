from fastapi import FastAPI
from app.core.config.settings import settings
from app.core.exceptions.handlers import register_exception_handlers
from app.modules.settings.router import router as settings_router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.modules.users.routers.auth_router import router as auth_router
from app.modules.users.routers.user_router import router as users_router
from app.modules.users.routers.role_router import router as role_router
from app.modules.academic_year.routers.academic_year_router import router as academic_year_router
from app.modules.classroom.routers.classroom_router import router as classroom_router
from app.modules.section.routers.section_router import router as section_router
from app.modules.student.routers.student_router import router as student_router
from app.modules.parent.routers.parent_router import router as parent_router
from app.modules.teacher.routers.teacher_router import router as teacher_router
from app.modules.attendance.routers.attendance_router import (
    router as attendance_router,
)
from app.modules.dashboard.routers.dashboard_router import (
    router as dashboard_router,
)
from app.modules.homepage.routers.homepage_router import (
    router as homepage_router,
)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Accept all origins
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

register_exception_handlers(app)

app.include_router(settings_router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(role_router)
app.include_router(academic_year_router)
app.include_router(classroom_router)
app.include_router(section_router)
app.include_router(student_router)
app.include_router(parent_router)
app.include_router(teacher_router)
app.include_router(attendance_router)
app.include_router(dashboard_router)
app.include_router(homepage_router)

@app.get("/", include_in_schema=False)
def root():
    return {"message": "School Management System API"}
