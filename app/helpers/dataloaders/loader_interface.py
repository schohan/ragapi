from abc import ABC, abstractmethod
from langchain_core.documents import Document
from typing import List

class LoaderInterface(ABC):
    @abstractmethod
    def load(self, filename: str):
        """Loads file in the given path for processing
        """
        pass
    
    @abstractmethod
    def extract(self) -> None | List:
        """Returns the content of the loaded file in the specified format"""
        pass 
    