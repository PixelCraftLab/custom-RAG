from fastapi import APIRouter
from pydantic import BaseModel

from app.chat import generate_answer
from app.embeddings import get_embedding_model
from app.models.schemas import ChatRequest, ChatResponse
from app.vectorstore import load_vector_store

router = APIRouter()

embedding_model = get_embedding_model()
# vector_store = load_vector_store(embedding_model)


#lasy lode
# embedding_model = None
vector_store = None





# @router.post("/chat", response_model=ChatResponse)
# def chat(request: ChatRequest):

#     response = generate_answer(
#         question=request.question, 
#         vector_store=vector_store,
#     )

#     return response

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    # Load the vector store only when a chat request comes
    vector_store = load_vector_store(embedding_model)

    if vector_store is None:
        return {
            "answer": "No document uploaded.",
            "sources": []
        }

    return generate_answer(
        question=request.question,
        vector_store=vector_store,
    )