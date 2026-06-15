from sqlalchemy.orm import SessionLocal
from app.models.document_chunk import DocumentChunk


class DocumentChunkService:
    def save_chunks(
        document_id: int,
        chunks: list[str], db: SessionLocal
        ):
        for chunk_index, chunk_text in enumerate(chunks):