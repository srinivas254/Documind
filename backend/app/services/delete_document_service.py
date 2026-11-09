import sys
from qdrant_client import models
from app.models.qdrant_model import client, COLLECTION_NAME


def delete_document_by_filename(source: str):

    response = client.delete(
        collection_name=COLLECTION_NAME,
        points_selector=models.FilterSelector(
            filter=models.Filter(
                must=[
                    models.FieldCondition(
                        key="metadata.source",
                        match=models.MatchValue(value=source),
                    )
                ]
            )
        ),
        wait=True
    )

    return {
        "message": f"Document '{source}' deleted successfully"
    }


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Please provide a PDF filename!")
        sys.exit(1)

    source = sys.argv[1]
    result = delete_document_by_filename(source)

    print(result)