from pathlib import Path
import shutil

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
        detail="Only PDF files are allowed."
    )
    file_path = UPLOAD_DIRECTORY / file.filename

    if file_path.exists():
        raise HTTPException(
        status_code=409,
        detail="Document already exists."
    )
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
        file.file,
        buffer,
    )
    return {
        "filename": file.filename
    }