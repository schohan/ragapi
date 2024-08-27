from abc import ABC, abstractmethod
from pymongo.results import InsertOneResult
from pymongo.cursor import Cursor
from typing import Any

class Repository(ABC):
    """An interface for all database repositories
    """
    
    @staticmethod 
    @abstractmethod
    def insertOne(tableOrCollection: str, documentOrRecord: Any) -> InsertOneResult:
        pass        
    
    @staticmethod 
    @abstractmethod
    def getAll(tableOrCollection: str) -> Cursor:
        pass



