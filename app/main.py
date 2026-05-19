from fastapi import FastAPI
from app.core.config.settings import settings
from app.core.exceptions.handlers import register_exception_handlers
from app.modules.settings.router import router as settings_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

register_exception_handlers(app)

app.include_router(settings_router)

@app.get("/")
def root():
    return {"message": "School Management System API"}
