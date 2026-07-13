from openai import OpenAI

from app.prompt import SYSTEM_PROMPT
from app.retriever import retrieve_documents 


client = OpenAI()

def generate_answer(
    question: str,
    vector_store,
    k: int = 4,
    score_threshold: float = 0.20,
):
    """
    Generate an answer using the retrieved document chunks.
    """

    results = retrieve_documents(
        question=question,
        vector_store=vector_store,
        k=k,
    )
    


    relevant_documents = [
    document
    for document, score in results
    if score <= score_threshold
    ]

    if not relevant_documents:
        return {
        "answer": "I couldn't find the answer in the uploaded document.",
        "sources": [],
        }
    
    context = "\n\n".join(
    document.page_content
    for document in relevant_documents

    )

    