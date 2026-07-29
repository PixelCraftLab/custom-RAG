from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config import CHUNK_SIZE, CHUNK_OVERLAP

def split_documents(documents):
    """
    Split documents into smaller chunks while preserving context.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    chunks = splitter.split_documents(documents)

    total_chunks = len(chunks)

    for index, chunk in enumerate(chunks):


        chunk.metadata["chunk_index"] = index

        chunk.metadata["total_chunks"] = total_chunks

        chunk.metadata["chunk_id"] = (
            f"{chunk.metadata.get('source')}_{index}"
        )

        chunk.metadata["token_estimate"] = (
            len(chunk.page_content) // 4
        )

    return chunks  

