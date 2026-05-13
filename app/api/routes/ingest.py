from fastapi import APIRouter

router = APIRouter(prefix="/api/ingest", tags=["Ingestion"])


@router.post("/placeholder")
async def ingest_placeholder() -> dict[str, str]:
    return {
        "status": "not_implemented",
        "message": "Ingestion endpoint placeholder",
    }