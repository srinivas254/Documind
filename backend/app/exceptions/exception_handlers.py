from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.myExceptions import (
    InvalidUploadException
)

async def invalid_upload_exception_handler(
    request: Request,
    exc: InvalidUploadException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.detail
        }
    )
