from typing import List
import boto3
from langchain_aws import BedrockEmbeddings 


class EmbeddingService:
    llm_runtime = boto3.client(service_name="bedrock-runtime")

    embeddings = BedrockEmbeddings(client=llm_runtime, 
                                   model_id="amazon.titan-text-lite-v1",
                                   credentials_profile_name="default")
 
        
    @classmethod
    def embed_documents(cls, docs: List[str]) -> List[List[float]]:
        # Ensure that document is at max 80% smaller than context window size. 
        # as at least 20% will be required for the prompt. This percetage can be adjusted as needed.  
        return cls.embeddings.embed_documents(docs)            
        

    @classmethod
    def embed_query(cls, query: str) -> List[float]:
        return cls.embeddings.embed_query(query)

