
from qdrant_client import models
from app.models.qdrant_model import client, COLLECTION_NAME, SPARSE_VECTOR_NAME, TOP_K
from fastembed import SparseEmbedding

def retrieve_sparse_chunks(
    sparse_vector: SparseEmbedding,
    source: str
) -> list:
    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=models.SparseVector(
            indices=sparse_vector.indices.tolist(),
            values=sparse_vector.values.tolist(),
        ),
        using=SPARSE_VECTOR_NAME,
        query_filter=models.Filter(
            must=[
                models.FieldCondition(
                    key="metadata.source",
                    match=models.MatchValue(value=source),
                )
            ]
        ),
        limit=TOP_K,
        with_payload=True,
    )

    points = results.points

    return points
