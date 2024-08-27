from fileinput import filename
from app.helpers.dataloaders.loader_interface import LoaderInterface
from langchain_community.document_loaders import Docx2txtLoader
from typing import List
from langchain_core.documents import Document
 
class DocLoader(LoaderInterface):
    
    def load(self, filename):
        self.filename = filename
        print("Loading file: %s" % filename)
        
    def extract(self) -> List | None:
        print("Extracting file: %s" % self.filename)        
        # load the pdf and split it into chunks
        data = []
        try:            
            loader = Docx2txtLoader(self.filename)
            data = loader.load()
        except Exception as e:
            print("Error extracting file: %s" % e)
            return None
        
        return data
    
    
        
        

