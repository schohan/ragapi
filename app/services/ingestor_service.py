from pathlib import Path
from app.helpers.dataloaders.pdf_loader import PdfLoader
from app.common.extracted_page import ExtractedPage

class IngestorService:
    
    @staticmethod
    def ingest(dir: str):
        print("Ingesting dir: %s" % dir)
        
        
    def extract_file(self, file: str):
        print("Ingesting file " + file)
        pdfLoader = PdfLoader()
        pages = pdfLoader.load(file).extract()
        #print("Content ==>>>> %s " % pages[0])
        extractedPages = []
        for page in pages:
            #print("Content ==>>>> %s " % pages)
            extractedPage = ExtractedPage()
            extractedPage.from_pdf(page)
            print("Extracted page ===>>> " + str(extractedPage.pageNum))
            extractedPages.append(extractedPage)
            
        return extractedPages            
        
                