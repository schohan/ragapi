from importlib import metadata
from multiprocessing import process
from pathlib import Path
from pydoc import Doc
from app.db.MongoDBRepository import MongoDBRepository
from langchain_core.documents import Document
from app.services.embedding_service import EmbeddingService
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.services.vectordb_service import VectorDbService

from typing import Any, Dict, List

import logging
logger = logging.getLogger(__name__)

class TokenizerService:    
    max_page_size = 1
    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size=100,
        chunk_overlap=20,
        length_function=len,
        is_separator_regex=False,
    )
    
    @staticmethod
    def tokenize():
        print("Tokenizing ..." )
        page_count = 0        
        skip =  0

        while True: 
            unprocessed_documents = TokenizerService.get_unprocessed(skip, TokenizerService.max_page_size)
            fetch_size = len(unprocessed_documents)
            skip += fetch_size            
            page_count += fetch_size
            #logger.info("\n===>>>>> res ...: %s" % res)    
            TokenizerService.process_documents(unprocessed_documents)
                    
            # exit if no more pages to process
            if fetch_size == 0:
                break

        logger.info("Page Count: %s" % page_count)
        return page_count


    @staticmethod
    def process_documents(unprocessed_documents):
        """Process the documents by tokenizing text, creating embeddings and storing them in a vectordb"""
        
        for doc in unprocessed_documents:
            print("\n\n -->>> Processing doc: %s" % doc)
                # process the document
                
            metadata = doc.get("metadata", {})
            metadata["id"] = doc.get("_id")
            metadata["processed"] = True
                                            
                # tokenize the document
            text_list = TokenizerService.text_splitter.create_documents([doc.get("page_content", [])])    
            chunks = [text.page_content for text in text_list]
            #print("\n\n -->>> Processing chunks: %s" % chunks)

            embs = EmbeddingService.embed_documents(chunks)
            #logger.info("\n Embeds: %s" % len(embs))            
            VectorDbService.insert(chunks, embs)
        

    @staticmethod   
    def get_unprocessed(skip: int =0, limit: int = 10) -> List[Dict[str, Any]]:
        logger.info("Fetching data. skip:%i , limit:%i" % (skip, limit))
        # write pages to mongodb collection called pages
        docs = []
        try:
            docs =  MongoDBRepository.getAll("pages", skip, limit)        
        except Exception as e:
            logger.error("Error saving to db: %s" % e)
            pass                        
        return docs
        
    
