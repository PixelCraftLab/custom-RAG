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
    return {
        "filename": file.filename
    }