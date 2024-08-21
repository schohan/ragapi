from pathlib import Path
from app.helpers.dataloaders.pdf_loader import PdfLoader
from app.common.extracted_page import ExtractedPage

class TokenizerService:
    
    @staticmethod
    def tokenize(text: str):
        print("Tokenizing ...: %s" % text)
        
        
        
                