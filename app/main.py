from fastapi import FastAPI
from app.api.user import router as users_router
from app.api.document import router as docements_router


app = FastAPI(title="AI Knowledge Base")
app.include_router(users_router)
app.include_router(docements_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}


