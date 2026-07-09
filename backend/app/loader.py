from langchain_community.document_loaders import PyPDFDirectoryLoader


def load_documents(folder_path: str):


    loader = PyPDFDirectoryLoader(folder_path)

    documents = loader.load()
      
    return documents
  