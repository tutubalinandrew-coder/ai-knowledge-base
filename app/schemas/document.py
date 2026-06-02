from pydantic import BaseModel
from pydantic import ConfigDict

class DocumentCreate(BaseModel):
    user_id: int
    title: str 
    filename: str 
    file_path: str
    file_size: int | None
    processing_status: str

class DocumentRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    title: str 
    filename: str 
    file_path: str
    file_size: int | None
    processing_status: str