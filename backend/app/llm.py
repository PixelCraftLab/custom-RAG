from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq


load_dotenv()


# def get_llm():
#     """
#     Returns the Gemini LLM.
#     """

#     llm = ChatGoogleGenerativeAI(
#         model="gemini-2.5-flash",
#         temperature=0,
#     )

#     return llm  


def get_llm():
    """
    Returns the Groq LLM.
    """

    llm = ChatGroq(
        model="openai/gpt-oss-120b", 
        # model="llama-3.1-8b-instant",  
        temperature=0,  
    )

    return llm   

