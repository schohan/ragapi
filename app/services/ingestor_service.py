from pathlib import Path
from pydoc import doc

import logging
from langchain_core.documents import Document

from app.db.MongoDBRepository import MongoDBRepository
logger = logging.getLogger(__name__)


import requests
from app.helpers.dataloaders.pdf_loader import PdfLoader
from app.helpers.dataloaders.doc_loader import DocLoader
from app.common.extracted_page import ExtractedPage
from app.config import settings

from typing import List

class IngestorService:
    
    @staticmethod
    def ingest_dir(dir: str):
        print("Ingesting dir: %s" % dir)
        pass
        
        
    def ingest(self, files: List[str] | None, file_type: str | None, is_local: bool = True) -> List[ExtractedPage]:
        print("Ingesting files: " + str(files))
        
        pages = []        
        if files is not None:
            for file in files:
                self.ingest_file(file, str(settings.data_sources.get("out_dir")))
    
        print("Extracted pages: " + str(pages))    
        return pages            
        

    def ingest_file(self, file: str, out_dir: str) -> List[Document] | None:
        print("ingest_file : %s" % (file))
        pages: List[Document] = []
        if file.endswith('.pdf'):
            print("Extracting pdf file: %s" % file)
            pdfLoader = PdfLoader()
            pdfLoader.load(file)
            pages = pdfLoader.extract()
        elif file.endswith('.docx'):
            print("Extracting docx file: %s" % file)
            docLoader = DocLoader()
            docLoader.load(file)
            pages= docLoader.extract()

        return pages

    def save_to_db(self, pages: List[Document]):
        logger.info("Saving to db: %s" % pages)
        # write pages to mongodb collection called pages
        for page in pages:
            toSave = page.dict()
            toSave["_id"] = (page.metadata["source"] + "_") + (str(page.metadata["page"]) if page.metadata.get("page") else " ")
            try:
                # Save each page to the database
                # Assuming you have a MongoDB client instance called "client"
                MongoDBRepository.insertOne("pages", toSave)
            except Exception as e:
                logger.error("Error saving to db: %s" % e)
                pass                