from pathlib import Path
from fastapi import APIRouter, Query, Response
from fastapi.responses import StreamingResponse
#from app.helpers.dataloaders.pdf_loader import PdfLoader
#from app.services.ingestor_service import IngestorService
from app.services.llm_service import LlmService
from app.services.bedrock_service import BedrockService
import json
from fastapi.encoders import jsonable_encoder
from typing import Annotated
from markdown import markdown
from app.services.vectordb_service import VectorDbService

router = APIRouter(
    prefix="/inferer",
    tags=["inferer"],
    responses={404: {"description": "Not found!!"}}
)


@router.get("/")
async def infer(q: Annotated[str | None, Query(max_length=100)] = None):
    if q:        
        return LlmService.test(q)
    else:
        return "No query specified" 


@router.get("/list-bedrock-models")
async def list_bedrock_models(q: Annotated[str | None, Query(max_length=100)] = None):
    return BedrockService.list_models()


@router.get("/search-similar")
def search_similar(q: str, stream: bool = False):   
    print("Searching for similar documents to: %s" % q)

    docs = VectorDbService.search(q, 50)
    
    print("Found documents: %s" % str(docs))
    
    context_prompt = create_context_prompt(docs, q)
    
    print("context_prompt: %s" % context_prompt)

    # Stream the response, if requested
    if ( stream ):
        return StreamingResponse(LlmService.stream(context_prompt), media_type="text/plain")
    
    # Otherwise, return the response as a string
    resp =  LlmService.call(context_prompt)
    return Response(content=resp, media_type="text/plain")





@router.get("/test")
async def infertest(q: Annotated[str | None, Query(max_length=100)] = None):
    if q:
        return LlmService.test(q)
    else:
        return "No query specified" 



def create_context_prompt(docs, query):
    context = "Using the following context: \n ---- \n "
    for doc in docs:
        context += doc.page_content + " "
    context += " --- "
    context += " answer the following question: \n ---- \n"
    context += query

    return context