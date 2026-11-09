from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from app.routers.primary import router as primary_router
from app.exceptions.myExceptions import (
    InvalidUploadException
)
from app.exceptions.exception_handlers import (
    invalid_upload_exception_handler
)

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(primary_router)

app.add_exception_handler(
    InvalidUploadException,
    invalid_upload_exception_handler
    )




