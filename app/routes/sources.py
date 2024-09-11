from fastapi import APIRouter
from app.config import settings
from app.services.ingestor_service import IngestorService

router = APIRouter(
    prefix="/sources",
    tags=["sources"],
    responses={404: {"description": "Not found!!"}}
)


@router.get("/")
async def sources():
    # content = IngestorService().ingest(settings.data_sources.get("google_files"), 'docx', False)
    return {"files": settings.data_sources}
