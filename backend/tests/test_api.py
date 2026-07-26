"""Tests for the backend foundation endpoints."""

from app.core.config import Settings
from app.main import create_app
from fastapi.testclient import TestClient


def test_health_returns_healthy_status() -> None:
    client = TestClient(create_app())

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_version_returns_configured_application_identity() -> None:
    settings = Settings(app_name="Test Agent", app_version="9.8.7")
    client = TestClient(create_app(settings))

    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {"name": "Test Agent", "version": "9.8.7"}
