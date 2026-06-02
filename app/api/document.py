
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.models import document
from app.schemas.document import DocumentCreate, DocumentRead
from app.models.document import Document
from app.core.database import get_db


router = APIRouter()

@router.post("/documents", response_model=DocumentRead)
def create_document(document_data: DocumentCreate, db: Session = Depends(get_db)):
    new_document = Document(
        user_id=document_data.user_id,
        title=document_data.title,
        filename=document_data.filename,
        file_path=document_data.file_path,
        file_size=document_data.file_size,
        processing_status=document_data.processing_status,
        )
    db.add(new_document)
    db.commit()
    db.refresh(new_document)
    return new_document

@router.post("/upload", response_model=DocumentRead)
async def  upload_file(                 
    user_id: int,
    file: UploadFile = File(...), 
    db: Session = Depends(get_db)
):
    filename = file.filename
    path = f"uploads/{file.filename}"
    contents = await file.read()
    file_size = len(contents)

    with open(path, "wb") as buffer:
        buffer.write(contents)

    
    
    new_document = Document(
        user_id=user_id,
        title=filename,
        filename=filename,
        file_path=path,
        file_size=file_size,
        processing_status = "pending"
    )
    db.add(new_document)
    db.commit()
    db.refresh(new_document)    
    return new_document
    

