from app.vector_search import vector_search
from app.bm25_loader import load_bm25
from app.rrf import reciprocal_rank_fusion


def hybrid_retrieve(
    question: str,
    vector_store,
    k: int,
):
    dense_results = vector_search(
        question=question,
        vector_store=vector_store,
        k=k,
    )

    bm25 = load_bm25()

    bm25_results = bm25.search( 
        question,
        k=k,
    )

    fused_results = reciprocal_rank_fusion(
        dense_results,
        bm25_results,
    )

    return fused_results[:k]