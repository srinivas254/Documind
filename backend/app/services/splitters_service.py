from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents: list[dict]) -> list[Document]:

    # Convert dictionaries into LangChain Document objects
    langchain_documents = [
        Document(
            page_content=doc["page_content"],
            metadata=doc["metadata"]
        )
        for doc in documents
    ]

    # Create the splitter object
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50
    )

     # Split the documents
    chunks = splitter.split_documents(langchain_documents)

    return chunks