from fastapi import APIRouter
router = APIRouter(prefix="/ingest", tags=["ingest"])

@router.get("/")
async def injest_placeholder():
    return {"ingest route placeholder"}