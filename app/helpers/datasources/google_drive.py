from typing import overload
from typing import List
from base_source import BaseDataSource


class GoogleDrive(BaseDataSource):
    """ Class to fetch files from given google drive location """

    

    def readAll(self, path: str) -> List[str]:

        return []
