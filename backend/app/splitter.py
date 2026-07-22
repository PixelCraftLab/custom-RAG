from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Split documents into smaller chunks while preserving context.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=500,
    )

    chunks = splitter.split_documents(documents)

    return chunks 

