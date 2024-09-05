import boto3

class BedrockService:
    llm = boto3.client(
        service_name="bedrock"
    )
      
    @classmethod
    def list_models(cls):
        return cls.llm.list_foundation_models()
