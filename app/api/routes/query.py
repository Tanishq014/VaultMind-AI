from fastapi import APIRouter

router = APIRouter(prefix="/api/query", tags=["Query"])


@router.post("/placeholder")
async def query_placeholder() -> dict[str, str]:
    return {
        "status": "not_implemented",
        "message": "Query endpoint placeholder",
    }