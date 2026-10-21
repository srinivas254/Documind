
from fastapi import APIRouter, File, UploadFile, Depends
from pathlib import Path
from tempfile import NamedTemporaryFile

from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
    CSVLoader,
)

from app.services.loaders_service import process_document
from app.services.splitters_service import split_documents
from app.services.dense_embeddings_service import dense_embed_documents
from app.services.sparse_embeddings_service import sparse_embed_documents
from app.services.qdrant_service import store_points
from app.services.dense_retrieval_service import retrieve_dense_chunks
from app.services.sparse_retrieval_service import retrieve_sparse_chunks
from langchain_core.documents import Document
from app.services.rrf_service import reciprocal_rank_fusion
from app.services.llm_service import llm_retrieval

from app.models.request_model import (
    UploadDocumentRequest,
    UserQueryRequest
)
from app.models.response_model import (
    UploadDocumentResponse,
    UserResponse
)

router = APIRouter()


@router.post("/upload", response_model= UploadDocumentResponse)
async def upload_document(request: UploadDocumentRequest = Depends()):
    file = request.file
    documents = await process_document(file)
    chunks = split_documents(documents)
    dense_vectors = dense_embed_documents(chunks)
    sparse_vectors = sparse_embed_documents(chunks)
    response = store_points(chunks, dense_vectors, sparse_vectors)

    return UploadDocumentResponse(
        message = response
    )

@router.post("/retrieve", response_model= UserResponse)
async def retrieve_answer(request: UserQueryRequest):
    query = [request.query]
    query_document = Document(page_content=query[0])
    dense_vectors = dense_embed_documents([query_document])
    sparse_vectors = sparse_embed_documents([query_document])
    dense_results = retrieve_dense_chunks(dense_vector=dense_vectors[0],  source=request.source)
    sparse_results = retrieve_sparse_chunks( sparse_vector=sparse_vectors[0], source=request.source)
    content = reciprocal_rank_fusion(dense_results, sparse_results)
    context = "\n\n".join(content)
    response = llm_retrieval(context, query[0])

    return UserResponse(
        answer = response
    )

