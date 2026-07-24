# # from openai import OpenAI

# from app.llm import get_llm

# from app.prompt import SYSTEM_PROMPT
# from app.retriever import retrieve_documents 
# from app.memory import (add_user_message, add_assistant_message, get_conversation, add_retrieved_chunks)

# # client = OpenAI()

# def generate_answer(
#     question: str,
#     vector_store,
#     k: int = 10,
#     # score_threshold: float = 0.20,
# ):
#     """
#     Generate an answer using the retrieved document chunks.
#     """

#     add_user_message(question)

#     results = retrieve_documents(
#         question=question,
#         vector_store=vector_store,
#         k=k,
#     )
#     add_retrieved_chunks(results)
   
#     print("\nRetrieved Results:")
#     for i, (doc, score) in enumerate(results, start=1):
#         print(f"{i}. Score: {score:.4f}")
#         print(doc.page_content[:120])
#         print("-" * 50)
    


#     relevant_documents = [
#     document
#     for document, score in results
#     # if score <= score_threshold
#     ]

#     if not relevant_documents:
#         return {
#         "answer": "Sorry, I couldn't find the answer in the uploaded document. Vishal who built me has strictly grounded me.",
#         "sources": [],
#         }
    
#     context = "\n\n".join(
#     document.page_content
#     for document in relevant_documents

#     )

#     history_parts = []

# for message in get_conversation():

#     if message["role"] == "user":
#         history_parts.append(
#             f"User: {message['content']}"
#         )

#     elif message["role"] == "assistant":
#         history_parts.append(
#             f"Assistant: {message['content']}"
#         )

#     elif message["role"] == "retrieval":

#         chunks = "\n".join(
#             chunk["content"]
#             for chunk in message["chunks"]
#         )

#         history_parts.append(
#             f"Retrieved Document Chunks:\n{chunks}"
#         )

#     history = "\n\n".join(history_parts)

#     prompt = SYSTEM_PROMPT.format(
#     context=context,
#     history=history,
#     question=question,
#     )

#     llm = get_llm()



#     response = llm.invoke(prompt)

#     answer = response.content
#     add_assistant_message(answer)


#     sources = [
#     {
#         "source": document.metadata.get("source"),
#         "page": document.metadata.get("page"),
#     }
#     for document in relevant_documents
#     ]

#     return {
#         "answer": answer,
#         "sources": sources,
#     }

from app.llm import get_llm
from app.prompt import SYSTEM_PROMPT
from app.retriever import retrieve_documents
from app.memory import (
    add_user_message,
    add_assistant_message,
    add_retrieved_chunks,
    get_conversation,
)


def generate_answer(
    question: str,
    vector_store,
    k: int = 5,
):
    """
    Generate an answer using the retrieved document chunks.
    """

    add_user_message(question)

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
    ]

    if not relevant_documents:
        return {
            "answer": "Sorry, I couldn't find the answer in the uploaded document. Vishal who built me has strictly grounded me.",
            "sources": [],
        }

    context = "\n\n".join(
        document.page_content
        for document in relevant_documents
    )


    history_parts = []

    for message in get_conversation():

        if message["role"] == "user":
            history_parts.append(
                f"User: {message['content']}"
            )

        elif message["role"] == "assistant":
            history_parts.append(
                f"Assistant: {message['content']}"
            )

        elif message["role"] == "retrieval":

            chunks = "\n".join(
                chunk["content"][:150] + "..."
                for chunk in message["chunks"]
            )

            history_parts.append(
                f"Previous Retrieved Chunks:\n{chunks}"
            )

    history = "\n\n".join(history_parts)

    prompt = SYSTEM_PROMPT.format(
        history=history,
        context=context,
        question=question,
    )

    llm = get_llm()

    response = llm.invoke(prompt)

    answer = response.content

    add_retrieved_chunks(results)

    add_assistant_message(answer)

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