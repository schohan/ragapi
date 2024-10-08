from app.helpers.dataloaders.loader_interface import LoaderInterface
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from typing import List
 
class PdfLoader(LoaderInterface):
    
    def load(self, filename):
        self.filename = filename
        print("Loading file: %s" % filename)
        
    def extract(self) -> List[Document] | None:
        print("Extracting file: %s" % self.filename)        
        # load the pdf and split it into chunks
        try:
            #loader = OnlinePDFLoader(self.filename)
            #data = loader.load()
            loader = PyPDFLoader(self.filename)
            data = loader.load_and_split()
        except Exception as e:
            print("Error extracting file: %s" % e)
            return None
        else:                
            return data
    
    
        
        

