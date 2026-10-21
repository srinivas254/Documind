from pydantic import BaseModel

class UploadDocumentResponse(BaseModel):
    message: str

class UserResponse(BaseModel):
    answer: str