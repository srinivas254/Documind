from pydantic import BaseModel
from fastapi import UploadFile, File

class UploadDocumentRequest:
    def __init__(self, file: UploadFile = File(...)):
        self.file = file

class UserQueryRequest(BaseModel):
    query: str
    source: str 