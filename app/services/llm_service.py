from langchain_community.llms import Ollama
from app.config import model_settings

class LlmService:
    llm = Ollama(
            base_url=model_settings.llama3.get("url"),
            model="llama3"
        )
    url = model_settings.llama3.get("url")       

    @classmethod
    def test(cls, question):        
        print("Url : " + url)
        resp = cls.llm.invoke(question)
        print(resp)
        return resp

    @classmethod
    def call(cls, prompt, question):
        print(f"Calling with prompt: {prompt} Question: {question}")
        resp = cls.llm.invoke(question)
        print(resp)
        return resp
      
