from sqlalchemy import BigInteger, Column, DateTime, Text, func


from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)

    telegram_id = Column(
        BigInteger,
        unique=True,
        nullable=False
    )

    username = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )