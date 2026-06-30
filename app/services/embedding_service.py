from app.core.config import settings 
from openai import OpenAI

from app.core.database import get_db
from app.models.document_chunk import DocumentChunk
from app.services.document_chunk_service import DocumentChunkService
from sqlalchemy.orm import Session
from sklearn.metrics.pairwise import cosine_similarity



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

class SemanticSearchService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.document_chunk_service = DocumentChunkService()

    def search(
        self,
        question: str,
        db: Session
    )-> list[str]:
        if not question.strip():
            raise ValueError("Text is empty")

        question_embedding = self.embedding_service.generate_embedding(question)
        chunks = self.document_chunk_service.get_all_chunks(db)
        similarities = []
        for chunk in chunks:
            if chunk.embedding is None:
                continue
        
            similarity = cosine_similarity(
                [question_embedding],
                [chunk.embedding]
            )[0][0]

            similarities.append(
                (chunk, similarity)
            )
        similarities.sort(
        key=lambda x: x[1],
        reverse=True
        ) 
        top_chunks = [
            chunk.text
            for chunk, similarity in similarities[:3]
        ]    



class RAGService:

    def __init__(self):
        self.search_service = SemanticSearchService()
        self.answer_service = AnswerService()

    def ask(
        self,
        question: str,
        db: Session
    )-> str:
        chunks = self.search_service.search(question)
        answer = self.answer_service.generate_answer(
            question=question,
            chunks=chunks,
        )
        return answer

class AnswerService:

    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY
        )
        self.model = settings.CHAT_MODEL

    def generate_answer(
        self,
        question: str,
        chunks: list[str]
    ) -> str:
        if not question.strip():
            raise ValueError("Question is empty")
        context = "\n\n".join(chunks)

        prompt = f"""
        Контекст:
        {context}

        Вопрос:
        {question}
        Ответь на вопрос, используя только информацию из контекста.
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Отвечай только на основе предоставленного контекста. "
                        "Если ответа в контексте нет, так и скажи. "
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        answer = response.choices[0].message.content
        return answer