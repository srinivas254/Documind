from qdrant_client import models
from app.models.qdrant_model import client, COLLECTION_NAME, DENSE_VECTOR_NAME, TOP_K

def retrieve_dense_chunks(
    dense_vector: list[float],
    source: str,
) -> list:

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=dense_vector,
        using=DENSE_VECTOR_NAME,
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