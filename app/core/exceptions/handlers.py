from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


async def generic_exception_handler(
    request: Request,
    exc: Exception,
):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": str(exc),
        },
    )


def register_exception_handlers(app: FastAPI):
    app.add_exception_handler(
        Exception,
        generic_exception_handler,
    )
