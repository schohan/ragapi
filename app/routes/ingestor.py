from pathlib import Path
from fastapi import APIRouter, Query
from app.config import settings
from app.helpers.dataloaders.pdf_loader import PdfLoader
from app.services.ingestor_service import IngestorService
from app.services.llm_service import LlmService
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
    local_dirs = settings.data_sources.get("dir")

    # todo: implement this method
    #IngestorService.ingest(localDirs)

    print ("Processing Local Dirs from list: %s" % local_dirs)
    
    # process each local directory
    for dir_path in local_dirs:
        print ("dir: %s" % dir_path)
        directory = Path(dir_path)
        content = []
        ingestor_service = IngestorService()
        # Pricess PDF fles in this directory
        for file_path in directory.rglob('*.pdf'):
            print ("Processing file path %s" % file_path.absolute())
            
            if file_path.is_file():
                print("Ingesting file " + file_path.absolute().name)
                extracted_pages = ingestor_service.extract_file(str(file_path.absolute()))
                content.append(extracted_pages)
            
    return {"data": jsonable_encoder(content)}


@router.get("/infertest")
async def infertest(q: Annotated[str | None, Query(max_length=100)] = None):
    if q:
        return LlmService.test(q)
    else:
        return "No query specified" 
