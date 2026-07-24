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


        metadata = chunk.metadata.copy() 

        metadata.update({
            "chunk_id": f"{metadata.get('source', 'doc')}_{index}",
            "chunk_index": index,
            "total_chunks": total_chunks,
            "char_count": len(chunk.page_content),
            "token_estimate": len(chunk.page_content) // 4,
        })

        chunk.metadata = metadata

    return chunks 

