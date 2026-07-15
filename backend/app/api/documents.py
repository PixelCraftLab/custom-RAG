from pathlib import Path
from fastapi import APIRouter, HTTPException
from datetime import datetime

from app.embeddings import get_embedding_model
from app.vectorstore import delete_document_vectors

router = APIRouter()

UPLOAD_DIRECTORY = Path("data/uploads")

@router.get("/documents")
def list_documents():
    documents = []

    for file in UPLOAD_DIRECTORY.glob("*.pdf"):

        documents.append(
            {
                "filename": file.name,
                "size_kb": round(file.stat().st_size / 1024, 2),
                "uploaded_at": datetime.fromtimestamp(
                    file.stat().st_mtime
                ).strftime("%Y-%m-%d %H:%M:%S"),
            }
        )

    return {
        "total_documents": len(documents),
        "documents": documents,
    }





@router.delete("/documents/{filename}")
def delete_document(filename: str):

    file_path = UPLOAD_DIRECTORY / filename

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Document not found."
        )

    embedding_model = get_embedding_model()

    delete_document_vectors(
        embedding_model=embedding_model,
        source=str(file_path),
    )

    file_path.unlink()

    return {
        "message": "Document deleted successfully.",
        "filename": filename,
    }