from pathlib import Path
from fastapi import APIRouter, Query, Response
from app.helpers.dataloaders.pdf_loader import PdfLoader
from app.services.ingestor_service import IngestorService
from app.services.llm_service import LlmService
from app.services.bedrock_service import BedrockService
import json
from fastapi.encoders import jsonable_encoder
from typing import Annotated
from markdown import markdown

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


@router.get("/withprompt")
async def infer_with_prompt(prompt:str|None = "default", q: Annotated[str | None, Query(max_length=100)] = None):    
    if q:
        resp = LlmService.call(prompt, q)
        html_content = markdown(resp)
        return Response(content=html_content, media_type="text/html")
    else:
        return "No query specified" 


@router.get("/test")
async def infertest(q: Annotated[str | None, Query(max_length=100)] = None):
    if q:
        return LlmService.test(q)
    else:
        return "No query specified" 
