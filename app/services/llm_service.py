from langchain_community.llms import Ollama
from app.config import model_settings

class LlmService:
    llm = Ollama(
            base_url=model_settings.model.get("url"),
            model=model_settings.model.get("name"),
        )



    @classmethod
    def test(cls, question):        
        print("question : " + question)
        resp = cls.llm.invoke(question)
        print(resp)
        return resp

    @classmethod
    def call(cls, context_prompt_query):
        resp = cls.llm.invoke(context_prompt_query)
        return resp
      
