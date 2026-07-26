"""Foundation API endpoints."""

from fastapi import APIRouter, Request

from app.core.config import Settings
from app.models.status import HealthResponse, VersionResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse, tags=["system"])
async def health() -> HealthResponse:
    """Report whether the API process is healthy."""
    return HealthResponse(status="healthy")


@router.get("/version", response_model=VersionResponse, tags=["system"])
async def version(request: Request) -> VersionResponse:
    """Return identifying information for this API."""
    settings: Settings = request.app.state.settings
    return VersionResponse(name=settings.app_name, version=settings.app_version)
