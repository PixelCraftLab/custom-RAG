# from openai import OpenAI

from app.llm import get_llm

from app.prompt import SYSTEM_PROMPT
from app.retriever import retrieve_documents 


# client = OpenAI()

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
   
    print("\nRetrieved Results:")
    for i, (doc, score) in enumerate(results, start=1):
        print(f"{i}. Score: {score:.4f}")
        print(doc.page_content[:120])
        print("-" * 50)
    


    relevant_documents = [
    document
    for document, score in results
    # if score <= score_threshold
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

    prompt = SYSTEM_PROMPT.format(
    context=context,
    question=question,
    )

    llm = get_llm()



    response = llm.invoke(prompt)

    answer = response.content


    sources = [
    {
        "source": document.metadata.get("source"),
        "page": document.metadata.get("page"),
    }
    for document in relevant_documents
    ]

    return {
        "answer": answer,
        "sources": sources,
    }

    