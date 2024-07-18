from fastapi import APIRouter
from app.config import settings

router = APIRouter(
    prefix="/sources",
    tags=["sources"],
    responses={404: {"description": "Not found!!"}}
)


@router.get("/")
async def sources():
    return {"sources": settings.data_sources.get("dir")}