from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.ingest import router as ingest_router
from app.api.routes.query import router as query_router
from app.core.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description="AI microservice powering VaultMind RAG workflows",
    )

    app.include_router(health_router)
    app.include_router(ingest_router)
    app.include_router(query_router)

    return app


app = create_app()