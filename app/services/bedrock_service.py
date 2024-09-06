from typing import List
import boto3
from langchain_aws import BedrockEmbeddings

class BedrockService:
    llm = boto3.client(
        service_name="bedrock"
    )

    bedrk_embeddings = BedrockEmbeddings(client=llm, 
        credentials_profile_name="default", region_name="us-east-1"
    )
      
    @classmethod
    def list_models(cls):
        return cls.llm.list_foundation_models()

    @classmethod
    def embed_documents(cls, docs: List[str]) -> List[List[float]]:
        return cls.bedrk_embeddings.embed_documents(docs)
    
