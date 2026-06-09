
from sqlalchemy import BigInteger, Column, ForeignKey, Text, UniqueConstraint
from app.core.database import Base
from sqlalchemy.orm import relationship


class DocumentChunk(Base):
    __tablename__ = "document_chunks"
    id = Column(BigInteger, primary_key=True, autoincrement=True) 
    document_id = Column (BigInteger,ForeignKey("documents.id"), nullable=False)
    chunk_index = Column(BigInteger, nullable=False)
    text = Column(Text, nullable=False)

    __table_args__ = (
        UniqueConstraint('document_id', 'chunk_index', name='uq_document_chunk_index'),
    )
    document = relationship("Document", back_populates="chunks",)