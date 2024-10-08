from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    """This class provides config/settings for the application.
    Model configuration:
    chunk_size - The chunk size of the text used by tokenizer.
    context_size - Used by retriever to ensure not more than this many tokens are passed as context as it is max limit of the model.
    TODO: A subclass should fetch configurations from the database for a given account.
    """
    app_name: str = "RAG API"
    mongodb_url: str = "mongodb://localhost:27017"
    data_sources: dict[str, list] = {
        "inp_dir": ["./data/inp/"],
        "google_files": []
    }
        
    # llama3: dict = {
    #     "url": "http://localhost:11434",
    #     "chunk_size": 1000, 
    #     "context_size": 8000, 
    # }
    
class ModelSettings(BaseSettings): 
    splitter : dict = {
        "chunk_size": 10, 
        "chunk_overlap": 3
    }
    embedding_models: dict = {
        #"name": "BAAI/bge-small-en"
        "name": "sentence-transformers/all-mpnet-base-v2"
    }       
    model: dict = {
        "name": "llama3.1:8b",
        "url": "http://localhost:11434",                 
        "context_size": 8000,
    }

    
settings = Settings()
model_settings = ModelSettings()