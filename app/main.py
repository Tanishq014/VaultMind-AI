from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.ingest import router as ingest_router
from app.api.routes.query import router as query_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="VaultMind AI Engine",
        version="0.1.0",
        description="AI microservice powering VaultMind RAG workflows",
    )

    app.include_router(health_router)
    app.include_router(ingest_router)
    app.include_router(query_router)

    return app


app = create_app()