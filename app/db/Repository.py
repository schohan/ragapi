from abc import ABC, abstractmethod

class Repository(ABC):
    """An interface for all database repositories
    """
    
    @abstractmethod
    def insertOne(self, tableOrCollection, documentOrRecord):
        pass        
    
    @abstractmethod
    def getAll(self,tableOrCollection):
        pass



