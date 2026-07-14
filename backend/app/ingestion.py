from app.loader import load_documents, load_document
from app.splitter import split_documents
from app.embeddings import get_embedding_model
from app.vectorstore import create_vector_store


def _ingest(
    documents,
    persist_directory="db",
):
    """
    Common ingestion pipeline.
    """

    chunks = split_documents(documents)

    embedding_model = get_embedding_model()

    vector_store = create_vector_store(
        chunks=chunks,
        embedding_model=embedding_model,
        persist_directory=persist_directory,
    )

    return vector_store

def ingest_documents(
    document_path="data/default",
    persist_directory="db"
):
    """
    Ingest all PDFs inside a folder.
    """

    documents = load_documents(document_path)

    return _ingest(
        documents,
        persist_directory,
    )


def ingest_document(
    file_path,
    persist_directory="db",
):
    """
    Ingest a single PDF.
    """

    documents = load_document(file_path)

    return _ingest(
        documents,
        persist_directory,
    )