from langchain_community.llms import Ollama
from app.config import model_settings

class LlmService:
    llm = Ollama(
            base_url=model_settings.model.get("url"),
            model=model_settings.model.get("name"),
        )

    @classmethod
    def call(cls, context_prompt_query):
        """Call the LLM model with the given context prompt query and return the response as a string"""
        resp = cls.llm.invoke(context_prompt_query)
        return resp

    
    @classmethod
    def stream(cls, context_prompt_query):
        """Stream the LLM model with the given context prompt query and stream the response"""
        resp = cls.llm.stream(context_prompt_query)
        return resp
      
