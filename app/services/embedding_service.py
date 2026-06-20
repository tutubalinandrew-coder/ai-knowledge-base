from app.core.config import settings 
from openai import OpenAI

class EmbeddingService:
    def __init__(self):
        self.model = settings.EMBEDDING_MODEL
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )
    def generate_embedding(
        self,
        text: str,
    )-> list[float]:
        if not text.strip():
            raise ValueError("Text is empty")

        response = self.client.embeddings.create(
        model=self.model,
        input=text
        )
        
        embedding = response.data[0].embedding
        return embedding


