from app.models.qdrant_model import client,COLLECTION_NAME, DENSE_VECTOR_NAME, SPARSE_VECTOR_NAME
from qdrant_client import models
from langchain_core.documents import Document
from fastembed import SparseEmbedding
from uuid import uuid4

def store_points(
    chunks: list[Document], 
    dense_vectors: list[list[float]],
    sparse_vectors: list[SparseEmbedding]
    ) -> str: 
    points = []

    for chunk, dense, sparse in zip(chunks, dense_vectors, sparse_vectors):
        point = models.PointStruct(
            id=str(uuid4()),
            vector={
                DENSE_VECTOR_NAME:dense,
                SPARSE_VECTOR_NAME:models.SparseVector(
                    indices=sparse.indices.tolist(),
                    values=sparse.values.tolist(),
                ),
            },
            payload={
                "text": chunk.page_content,
                "metadata": chunk.metadata,
            },
        )

        points.append(point)

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points,
        timeout=120,
    )

    return f"Inserted {len(points)} points successfully"
