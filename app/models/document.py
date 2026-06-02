from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Text, func
from app.core.database import Base


class Document(Base):
    __tablename__ = "documents"
 
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column (BigInteger,ForeignKey("users.id"), nullable=False)
    title = Column(Text)
    filename = Column(Text, nullable=False)
    file_path = Column(Text, nullable=False)
    file_size = Column(BigInteger)
    processing_status = Column(Text, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )