"""FastAPI application composition root."""

import logging

from fastapi import FastAPI

from app.api.routes import router
from app.core.config import Settings, get_settings
from app.core.logging import configure_logging


def create_app(settings: Settings | None = None) -> FastAPI:
    """Create and configure a FastAPI application instance."""
    resolved_settings = settings or get_settings()
    configure_logging(resolved_settings.log_level)

    application = FastAPI(
        title=resolved_settings.app_name,
        version=resolved_settings.app_version,
    )
    application.state.settings = resolved_settings
    application.include_router(router)

    logging.getLogger(__name__).info("application_configured")
    return application


app = create_app()
