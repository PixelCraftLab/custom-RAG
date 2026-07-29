from typing import List, Tuple

from langchain_core.documents import Document


def vector_search(
    question: str,
    vector_store,
    k: int,
) -> List[Tuple[Document, float]]:
    """
    Perform similarity search using ChromaDB.
    """

    results = vector_store.similarity_search_with_score(
        query=question,
        k=k,
    )

    return results