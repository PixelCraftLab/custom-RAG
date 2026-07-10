from fastapi import FastAPI
from app.loader import load_documents
from app.splitter import split_documents

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to Custom RAG API"
    }

@app.get("/documents")
def get_documents():
   
    documents = load_documents("data/default")

    result = [] 

    for doc in documents:
        result.append(
            {
 
                "source": doc.metadata.get("source"),
                "page": doc.metadata.get("page"),
                "characters": len(doc.page_content),
                "preview": doc.page_content[:200]
            }
        )

    return result


@app.get("/chunks")
def get_chunks():

    documents = load_documents("data/default")

    chunks = split_documents(documents)  

    result = []

    for index, chunk in enumerate(chunks): 
                          
        result.append(
            {
                "chunk_number": index + 1,
                "source": chunk.metadata.get("source"),
                "page": chunk.metadata.get("page"),
                "characters": len(chunk.page_content),
                "preview": chunk.page_content[:200]
            }   
        )

    return {                                
        "total_documents": len(documents),
        "total_chunks": len(chunks),
        "chunks": result
    }
