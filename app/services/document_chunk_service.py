from sqlalchemy.orm import Session
from app.models.document_chunk import DocumentChunk


class DocumentChunkService:
    def save_chunks(
        self,
        document_id: int,
        chunks: list[str], db: Session
        ):
        try:
            for chunk_index, chunk_text in enumerate(chunks):
                chunk = DocumentChunk(
                    document_id = document_id,
                    chunk_index = chunk_index,
                    text = chunk_text
                )
                db.add(chunk)
            db.commit()
        except Exception:
            db.rollback()
            raise

