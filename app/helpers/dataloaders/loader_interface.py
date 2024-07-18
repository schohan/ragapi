from abc import ABC, abstractmethod

class LoaderInterface(ABC):
    @abstractmethod
    def load(self, path: str):
        """Loads file in the given path for processing
        """
        pass
    
    @abstractmethod
    def extract(self, format: str):
        """Returns the content of the loaded file in the specified format"""
        pass 
    