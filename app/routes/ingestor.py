from pathlib import Path
from traceback import print_tb
from fastapi import APIRouter, Query
from typing import List
from app.config import settings
from app.helpers.dataloaders.pdf_loader import PdfLoader
from app.services.ingestor_service import IngestorService
from app.services.tokenizer_service import TokenizerService
from app.services.llm_service import LlmService
from app.services.embedding_service import EmbeddingService

import json
from fastapi.encoders import jsonable_encoder
from typing import Annotated

router = APIRouter(
    prefix="/ingestor",
    tags=["ingestor"],
    responses={404: {"description": "Not found!!"}}
)


@router.get("/ingest")
async def ingest():    
    local_dirs:List[str] = settings.data_sources.get("inp_dir", [])

    # todo: implement this method
    #IngestorService.ingest(localDirs)

    print ("Processing Local Dirs from list: %s" % local_dirs)
    
    content = []  # Initialize content here
    
    # process each local directory
    for dir_path in local_dirs:
        directory = Path(dir_path)
        content = []
        ingestor_service = IngestorService()
        
        print("current directory  %s" % directory.absolute())

        # Process fles in this directory
        for file_path in directory.iterdir():
            # skip non pdf or docx files
            if not file_path.name.endswith('.pdf') and not file_path.name.endswith('.docx'):
                continue

            print ("Processing file path %s" % file_path.absolute())
            
            if file_path.is_file():
                print("Ingesting file " + file_path.absolute().name)
                extracted_pages = ingestor_service.ingest_file(str(file_path.absolute()), str(settings.data_sources.get("out_dir")))
                
                # Save the extracted pages to the database
                ingestor_service.save_to_db(extracted_pages)

                # Append the extracted pages to the content to be returned
                content.append(extracted_pages)

    return {"data": jsonable_encoder(content)}




@router.get("/tokenize")
async def tokenize(text: str):    
    print("creating embeddings...")
    tokens = TokenizerService.tokenize(text)
    print("tokens: " + str(tokens)) 
    return {"message": "Tokens created", "tokens": tokens}


@router.get("/embeddings")
async def embeddings(text: str):    
    print("creating embeddings...")
    embs = EmbeddingService.embeddings(text)
    #print("embedding..." + str(embs[:2])) 
    return {"message": "Last embedding (as sample)", "embeddings": embs[:1]}
    






