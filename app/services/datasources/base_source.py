from abc import ABC, abstractmethod
from typing import List


class BaseDataSource(ABC):

    @abstractmethod
    def readAll(self, path: str) -> List[str]:
        # Read all the files from the given path. Path can be 

        pass


    