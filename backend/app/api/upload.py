from pathlib import Path
import shutil
from app.ingestion import ingest_document

from fastapi import APIRouter, File, HTTPException, UploadFile

router = APIRouter()

UPLOAD_DIRECTORY = Path("data/uploads")

UPLOAD_DIRECTORY.mkdir(
    parents=True,
    exist_ok=True,
)

@router.post("/upload")
def upload_pdf(
    file: UploadFile = File(...)
):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
        status_code=400,
        detail="Only PDF files are allowed for now, please wait for the next version update for other document type support."
    )
    file_path = UPLOAD_DIRECTORY / file.filename
 
    if file_path.exists():       
        raise HTTPException(
        status_code=409,
        detail="Document already exists, multiple entry not allowed."
    )
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
        file.file,
        buffer,

    )
        
    ingest_document(
    file_path=str(file_path)
    )
        
    return {
    "message": "Document uploaded successfully. You can start asking question structly grounded to document",
    "filename": file.filename,
    }
 