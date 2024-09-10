from langchain_core.documents import Document
from app.services.embedding_service import EmbeddingService
from langchain_chroma import Chroma
from app.config import model_settings

class VectorDbService:

    """Service class for VectorDb. TODO - create an interface for this class"""
    vectorstore = Chroma(embedding_function=EmbeddingService.get_embeddings(), persist_directory="./data/chroma_db")


    @classmethod
    def insert(cls, chunks: list[str], embeddings: list[list[float]]): 
        """Inserts documents into the vector store"""
        ids = cls.vectorstore.add_texts(chunks, embeddings=embeddings)
        print("Inserted into VectorStore ..." + str(ids))
    
    @classmethod
    def search(cls, query: str, k: int = 5) -> list[Document]:
        """Searches the vector store for the query"""
        print("Searching for query %s" % query)

        results = cls.vectorstore.similarity_search(query, k=k)
        print("Search results ..." + str(results))
        return results 