from app.loader import load_documents
from app.splitter import split_documents
from app.embeddings import get_embedding_model
from app.vectorstore import create_vector_store


def ingest_documents(
    document_path="data/default",
    persist_directory="db"
):
    """
    Complete ingestion pipeline:
    PDF -> Documents -> Chunks -> Embeddings -> ChromaDB
    """

    documents = load_documents(document_path)

    chunks = split_documents(documents)

    embedding_model = get_embedding_model()

    vector_store = create_vector_store(
        chunks=chunks,
        embedding_model=embedding_model,
        persist_directory=persist_directory,
    )

    return vector_store