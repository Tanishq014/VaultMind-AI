from fastapi import APIRouter

router = APIRouter(prefix="/query", tags=["query"])


@router.get("/")
async def query_placeholder():
    return {
        "message": "Query route placeholder"
    }