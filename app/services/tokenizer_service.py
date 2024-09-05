from pathlib import Path
from pydoc import Doc
from app.db.MongoDBRepository import MongoDBRepository
from langchain_core.documents import Document
from typing import Any, Dict, List

import logging
logger = logging.getLogger(__name__)

class TokenizerService:    
    max_page_size = 1

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
            logger.info("\n===>>>>> res ...: %s" % res)    
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
        
                