
import os

from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
    check_compatibility=False
)

COLLECTION_NAME = "documents_rag"

DENSE_VECTOR_NAME = "documents_dense_vector"
SPARSE_VECTOR_NAME = "documents_sparse_vector"

TOP_K = 3