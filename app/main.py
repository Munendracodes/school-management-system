from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_redoc_html
from fastapi.openapi.utils import get_openapi

from app.core.config.settings import settings
from app.core.exceptions.handlers import (
    register_exception_handlers,
)

# ==========================
# AUTH / USER MODULES
# ==========================

from app.modules.users.routers.auth_router import (
    router as auth_router,
)

from app.modules.users.routers.user_router import (
    router as users_router,
)

from app.modules.users.routers.role_router import (
    router as role_router,
)

# ==========================
# SETTINGS
# ==========================

from app.modules.settings.router import (
    router as settings_router,
)

# ==========================
# ACADEMIC MODULES
# ==========================

from app.modules.academic_year.routers.academic_year_router import (
    router as academic_year_router,
)

from app.modules.classroom.routers.classroom_router import (
    router as classroom_router,
)

from app.modules.section.routers.section_router import (
    router as section_router,
)

from app.modules.student.routers.student_router import (
    router as student_router,
)

from app.modules.parent.routers.parent_router import (
    router as parent_router,
)

from app.modules.teacher.routers.teacher_router import (
    router as teacher_router,
)

from app.modules.student_parent_map.routers.student_parent_map_router import (
    router as student_parent_mapping_router,
)

from app.modules.teacher_section_map.routers.teacher_section_map_router import (
    router as teacher_section_mapping_router,
)

# ==========================
# OPERATIONAL MODULES
# ==========================

from app.modules.attendance.routers.attendance_router import (
    router as attendance_router,
)

# ==========================
# DASHBOARD / HOMEPAGE
# ==========================

from app.modules.dashboard.routers.dashboard_router import (
    router as dashboard_router,
)

from app.modules.homepage.routers.homepage_router import (
    router as homepage_router,
)

from app.modules.homepage.routers.homepage_section_router import (
    router as homepage_section_router,
)

from app.modules.homepage.routers.homepage_item_router import (
    router as homepage_item_router,
)


# ====================================================
# API TAGS
# ====================================================

tags_metadata = [

    {
        "name": "🔐 Authentication",
        "description": "Login, logout, JWT and token APIs"
    },

    {
        "name": "👤 User Management",
        "description": "Users and role management"
    },

    {
        "name": "⚙️ School Settings",
        "description": "School configuration APIs"
    },

    {
        "name": "🏫 Academic Structure",
        "description": """
Academic hierarchy:

• Academic Year  
• Classroom  
• Section
"""
    },

    {
        "name": "🎓 Student Management",
        "description": """
Student operations:

• Student CRUD
• Parent mappings
"""
    },

    {
        "name": "👨‍👩‍👧 Parent Management",
        "description": "Parent operations"
    },

    {
        "name": "👨‍🏫 Teacher Management",
        "description": "Teacher operations"
    },

    {
        "name": "🔗 Mapping Engine",
        "description": """
Relationship APIs:

• Student Parent Mapping
• Teacher Section Mapping
"""
    },

    {
        "name": "📝 Attendance",
        "description": "Attendance APIs"
    },

    {
        "name": "📊 Dashboard",
        "description": "Dashboard analytics"
    },

    {
        "name": "🏠 Homepage Engine",
        "description": "Homepage rendering APIs"
    },

    {
        "name": "🎨 Homepage CMS",
        "description": "Homepage configuration APIs"
    }

]


# ====================================================
# FASTAPI APP
# ====================================================

app = FastAPI(

    title="🏫 School Management System API",

    version=settings.APP_VERSION,

    description="Comprehensive API for managing school operations, including students, teachers, attendance, and more.",

    openapi_tags=tags_metadata,

    contact={
        "name": "School ERP Team",
        "email": "support@schoolerp.com",
    },

    swagger_ui_parameters={

        "deepLinking": True,
        "displayRequestDuration": True,
        "docExpansion": "none",
        "defaultModelsExpandDepth": -1,
        "filter": False,
        "syntaxHighlight.theme": "obsidian",
    },

)


# ====================================================
# STATIC FILES
# ====================================================

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)


# ====================================================
# CUSTOM OPENAPI
# ====================================================

def custom_openapi():

    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    # optional logo
    openapi_schema["info"]["x-logo"] = {
        "url": "/static/logo.png"
    }

    app.openapi_schema = openapi_schema

    return app.openapi_schema


app.openapi = custom_openapi


# ====================================================
# CORS
# ====================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ====================================================
# EXCEPTION HANDLERS
# ====================================================

register_exception_handlers(app)


# ====================================================
# ROUTERS
# ====================================================

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

app.include_router(student_parent_mapping_router)

app.include_router(teacher_section_mapping_router)

app.include_router(attendance_router)

app.include_router(dashboard_router)

app.include_router(homepage_router)

app.include_router(homepage_section_router)

app.include_router(homepage_item_router)


# ====================================================
# CUSTOM REDOC
# ====================================================

@app.get(
    "/redoc",
    include_in_schema=False,
)
async def custom_redoc():

    return get_redoc_html(
        openapi_url=app.openapi_url,
        title="School ERP Documentation",
        with_google_fonts=True,
    )


# ====================================================
# ROOT
# ====================================================

@app.get(
    "/",
    include_in_schema=False,
)
def root():

    return {
        "message": "School Management System API 🚀"
    }