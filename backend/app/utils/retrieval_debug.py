
def print_retrieved_chunks(points: list, retrieval_type: str):

    print(f"\n{'=' * 70}")
    print(f"{retrieval_type.upper()} RETRIEVAL RESULTS")
    print(f"Total chunks retrieved: {len(points)}")
    print(f"{'=' * 70}")

    for i, point in enumerate(points, start=1):

        payload = point.payload or {}
        metadata = payload.get("metadata", {})

        print(f"\n--- CHUNK {i} ---")
        print(f"Point ID : {point.id}")
        print(f"Score    : {point.score}")
        print(f"Source   : {metadata.get('source')}")
        print(f"Metadata : {metadata}")
        print(f"Text     :\n{payload.get('text', 'No text found')}")

    print(f"\n{'=' * 70}\n")
