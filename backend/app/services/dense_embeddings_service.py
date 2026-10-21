from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings


embeddings_model = OllamaEmbeddings(
    model="nomic-embed-text"
)


def dense_embed_documents(chunks: list[Document]) -> list[list[float]]:
    texts = [chunk.page_content for chunk in chunks]

    vectors = embeddings_model.embed_documents(texts)

    return vectors