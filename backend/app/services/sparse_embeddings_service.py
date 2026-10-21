from app.models.qdrant_model import client,COLLECTION_NAME
from fastembed import SparseTextEmbedding, SparseEmbedding
from langchain_core.documents import Document

sparse_model = SparseTextEmbedding(
    model_name="Qdrant/bm25"
)

def sparse_embed_documents(chunks: list[Document]) -> list[SparseEmbedding]:
    texts = [chunk.page_content for chunk in chunks]

    sparse_vectors = list(sparse_model.embed(texts))

    return sparse_vectors