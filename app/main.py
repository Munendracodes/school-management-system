from fastapi import FastAPI
from app.core.config.settings import settings
from app.core.exceptions.handlers import register_exception_handlers
from app.modules.settings.router import router as settings_router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.modules.users.routers.auth_router import router as users_router
from app.modules.dashboard.routers.homepage_router import (
    router as homepage_router
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
app.include_router(users_router)
app.include_router(homepage_router)

@app.get("/")
def root():
    return {"message": "School Management System API"}
