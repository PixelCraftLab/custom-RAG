from langchain_chroma import Chroma


def create_vector_store(
    chunks,
    embedding_model,
    persist_directory="db",
):
    """
    Create and store embeddings in ChromaDB.
    """

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
    )

    return vector_store 

def load_vector_store(
    embedding_model,
    persist_directory="db",
):
    """
    Load an existing ChromaDB vector store.
    """

    vector_store = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_model,
    )

    return vector_store