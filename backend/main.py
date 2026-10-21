from fastapi import FastAPI 
from app.routers.primary import router as primary_router
from app.exceptions.myExceptions import (
    InvalidUploadException
)
from app.exceptions.exception_handlers import (
    invalid_upload_exception_handler
)

app = FastAPI()

app.include_router(primary_router)

app.add_exception_handler(
    InvalidUploadException,
    invalid_upload_exception_handler
    )




