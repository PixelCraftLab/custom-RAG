from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()


def get_embedding_model():
    """
    Returns the OpenAI embedding model.
    """

    embedding_model = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    return embedding_model 