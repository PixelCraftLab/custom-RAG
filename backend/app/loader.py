from langchain_community.document_loaders import PyPDFDirectoryLoader


def load_documents(folder_path: str):
    """
    Load all PDF files from a folder.
    """

    loader = PyPDFDirectoryLoader(folder_path)

    documents = loader.load()
      
    return documents
  