"""Vehicle availability states."""

from enum import StrEnum


class VehicleState(StrEnum):
    """The business-visible condition of a vehicle."""

    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    READY = "ready"
    FLYING = "flying"
    RETURNING = "returning"
    EMERGENCY = "emergency"
