from fastapi import UploadFile
from pathlib import Path
from tempfile import NamedTemporaryFile
from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
    CSVLoader,
)
from app.exceptions.myExceptions import (
    InvalidUploadException
)

SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".txt", ".csv", ".md"}


async def process_document(file: UploadFile) -> list[dict]:
    #validate filename and extension
    if not file.filename:
        raise InvalidUploadException(400, "Filename is required")

    extension = Path(file.filename).suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise InvalidUploadException(400, "Unsupported file type")

    temp_path = None
    
    try:

        # Read uploaded file bytes
        content = await file.read()

        if not content:
            raise InvalidUploadException(
                400, "Uploaded file is empty"
            )

        # Write bytes to a temporary file on disk
        with NamedTemporaryFile(
            suffix=extension,
            delete=False,
        ) as temp_file:
            temp_file.write(content)
            temp_path = Path(temp_file.name)

        # Select the appropriate LangChain loader
        if extension == ".pdf":
            loader = PyPDFLoader(str(temp_path))

        elif extension == ".docx":
            loader = Docx2txtLoader(str(temp_path))

        elif extension == ".csv":
            loader = CSVLoader(str(temp_path))

        else:
            # TXT and Markdown
            loader = TextLoader(str(temp_path),encoding="utf-8")

        # Extract document content
        try:
            documents = loader.load()

        except Exception as exc:
            raise InvalidUploadException(
                422, "Unable to process uploaded document"
            ) from exc

        if not documents:
            raise InvalidUploadException(
                422, "No content could be extracted"
            )

         #  Return extracted text and metadata
        return [
            {
                "page_content": doc.page_content,
                "metadata": {
                    **doc.metadata,
                    "source": file.filename,
                    "filetype": file.filename.split(".")[-1].lower(),
                },
            }
            for doc in documents
        ]

    finally:
        # Delete the temporary file
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)

        # Close the uploaded file
        await file.close()

        