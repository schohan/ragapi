from langchain_community.llms import Ollama
from app.config import settings
class LlmService:
    llm = Ollama(
            base_url=settings.models.get("llama3").get("url"),
            model="llama3"
        )
    url = settings.models.get("llama3").get("url")       

    @classmethod
    def test(cls, question):        
        print("Url : " + url)
        resp = cls.llm.invoke(question)
        print(resp)
        return resp

    @classmethod
    def call(cls, prompt, question):
        print("Calliong with prompt: {} Url: {} " % prompt, url)
        resp = cls.llm.invoke(question)
        print(resp)
        return resp
      