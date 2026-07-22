from langchain_core.documents import Document


def retrieve_documents(
    question: str,
    vector_store,
    k: int = 10, 
): 
    """
    Retrieve the most relevant document chunks
    along with their similarity scores.
    """

    results = vector_store.similarity_search_with_score(
        query=question,
        k=k, 
    )

    return results