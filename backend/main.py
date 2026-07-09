from fastapi import FastAPI
from app.loader import load_documents

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
