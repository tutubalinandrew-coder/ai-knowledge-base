import os


from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()




class Settings(BaseModel):
    OPENAI_API_KEY: str
    DATABASE_URL: str
    EMBEDDING_MODEL: str
    CHAT_MODEL: str 

settings = Settings(
    OPENAI_API_KEY=os.getenv("OPENAI_API_KEY"),
    DATABASE_URL=os.getenv("DATABASE_URL"),
    EMBEDDING_MODEL=os.getenv("EMBEDDING_MODEL"),
    CHAT_MODEL=os.getenv("CHAT_MODEL")
)