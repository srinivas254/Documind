from app.models.qdrant_model import TOP_K

def reciprocal_rank_fusion(dense_results: list, sparse_results: list) -> list[str]:
    combined_results = []
    k = 60

    #add id,point object, rrf score in a list
    for rank, point in enumerate(dense_results, start=1):
        combined_results.append({
            "id": len(combined_results) + 1,
            "point": point,
            "point_id": point.id,
            "rrf_score": 1 / (k + rank),
        })

    for rank, point in enumerate(sparse_results, start=1):
        combined_results.append({
            "id": len(combined_results) + 1,
            "point": point,
            "point_id": point.id,
            "rrf_score": 1 / (k + rank),
        })

    seen_ids = set()
    fused_results = {}

    #add only unique points in the dict by combining the RRF score
    for item in combined_results:
        point_id = item["point_id"]

        if point_id not in seen_ids:
            seen_ids.add(point_id)
            fused_results[point_id] = {
                "point": item["point"],
                "rrf_score": item["rrf_score"],
            }
        else:
            fused_results[point_id]["rrf_score"] += item["rrf_score"]

    #this returns a list of dict[point,rrf_score] first we take the values from the fused_results 
    #dict which is dict too & then we pass each dict object into lambda as an argument & return 
    # rrf score from it and we use this score as a key to sort this list in descending
    ranked_results = sorted(
        fused_results.values(),
        key=lambda item: item["rrf_score"],
        reverse=True,
    )

    #return top k ranked dict_values
    top_k_points = ranked_results[:TOP_K]

    content_chunks = [
    item["point"].payload["text"]
    for item in top_k_points
    ]

    return content_chunks
