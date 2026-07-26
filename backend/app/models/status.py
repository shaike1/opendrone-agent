"""Response models for service status endpoints."""

from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Health check response."""

    status: str


class VersionResponse(BaseModel):
    """Application identity response."""

    name: str
    version: str
