from pathlib import Path
from app.helpers.dataloaders.pdf_loader import PdfLoader
from app.common.extracted_page import ExtractedPage
from app.db.MongoDBRepository import MongoDBRepository

class EmbeddingService:
    
    @staticmethod
    def embeddings(text: str):
        print("Embeddings ...: %s" % text)
        return []
        
        
        
                