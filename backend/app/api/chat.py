from fastapi import APIRouter
from pydantic import BaseModel

from app.chat import generate_answer
from app.embeddings import get_embedding_model
from app.models.schemas import ChatRequest, ChatResponse
from app.vectorstore import load_vector_store

router = APIRouter()

embedding_model = get_embedding_model()
vector_store = load_vector_store(embedding_model)


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    response = generate_answer(
        question=request.question, 
        vector_store=vector_store,
    )

    return response