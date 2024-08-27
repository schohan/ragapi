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
    files = settings.data_sources.get("inp_dir")
    print(f"Returning sources:{files} ")
    # content = IngestorService().ingest(settings.data_sources.get("google_files"), 'docx', False)
    return {"files": files}
