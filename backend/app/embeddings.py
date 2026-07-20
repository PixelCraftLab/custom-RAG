# from dotenv import load_dotenv
# from langchain_openai import OpenAIEmbeddings

# load_dotenv()


# def get_embedding_model():
#     """
#     Returns the OpenAI embedding model.
#     """

#     embedding_model = OpenAIEmbeddings(
#         model="text-embedding-3-small"
#     )

#     return embedding_model 



from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    """
    Returns the Hugging Face embedding model.
    """

    embedding_model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5",
        model_kwargs={
            "device": "cpu"
 
        },
        encode_kwargs={
            "normalize_embeddings": True
        }
    )


    return embedding_model