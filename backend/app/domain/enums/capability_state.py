"""Capability availability states."""

from enum import StrEnum


class CapabilityState(StrEnum):
    """Whether a declared mission capability is available for use."""

    ENABLED = "enabled"
    DISABLED = "disabled"
