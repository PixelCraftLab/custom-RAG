from app.vector_search import vector_search


def hybrid_retrieve(
    question: str,
    vector_store,
    k: int,
):
    """
    Placeholder for hybrid retrieval.

    Currently uses only vector search.
    Later we'll add:
    - BM25
    - Merge
    - Reranker
    """

    return vector_search(
        question=question,
        vector_store=vector_store,
        k=k,
    )