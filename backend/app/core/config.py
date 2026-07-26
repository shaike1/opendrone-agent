"""Environment-backed application configuration."""

import os
from dataclasses import dataclass
from functools import lru_cache

DEFAULT_APP_NAME = "OpenDrone Agent"
DEFAULT_APP_VERSION = "0.1.0"
DEFAULT_LOG_LEVEL = "INFO"


@dataclass(frozen=True, slots=True)
class Settings:
    """Runtime settings for the backend service."""

    app_name: str = DEFAULT_APP_NAME
    app_version: str = DEFAULT_APP_VERSION
    log_level: str = DEFAULT_LOG_LEVEL


@lru_cache
def get_settings() -> Settings:
    """Load and cache settings from the process environment."""
    return Settings(
        app_name=os.getenv("APP_NAME", DEFAULT_APP_NAME),
        app_version=os.getenv("APP_VERSION", DEFAULT_APP_VERSION),
        log_level=os.getenv("LOG_LEVEL", DEFAULT_LOG_LEVEL).upper(),
    )
