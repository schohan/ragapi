from importlib import metadata
from multiprocessing import process
from pathlib import Path
from pydoc import Doc
from app.db.MongoDBRepository import MongoDBRepository
from langchain_core.documents import Document
from app.services.embedding_service import EmbeddingService
from langchain_text_splitters import RecursiveCharacterTextSplitter

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
            res = TokenizerService.get_unprocessed(skip, TokenizerService.max_page_size)
            fetch_size = len(res)
            skip += fetch_size            
            page_count += fetch_size
            #logger.info("\n===>>>>> res ...: %s" % res)    
            for doc in res:
                print("\n\n -->>> Processing doc: %s" % doc)
                # process the document
                
                
                metadata = doc.get("metadata", {})
                metadata["id"] = doc.get("_id")
                metadata["processed"] = True
                                            
                # tokenize the document
                docs1 = TokenizerService.text_splitter.create_documents([doc.get("page_content", [])])    
                chunks = [doc2.page_content for doc2 in docs1]
                print("\n\n -->>> Processing chunks: %s" % chunks)

                # embs = EmbeddingService.embed_documents([chunk.page_content for chunk in chunks])
                
                #logger.info("\n Embeds: %s" % embs)
                    
            # exit if no more pages to process
            if fetch_size == 0:
                break

        logger.info("Page Count: %s" % page_count)
        return page_count
        

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
        
                