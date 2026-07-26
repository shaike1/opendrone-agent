"""Contract checks for the public ports package."""

import app.ports as ports
from app.ports import Clock, EventPublisher, MissionStore, TelemetryPort, VehiclePort


def test_protocol_definitions_are_importable() -> None:
    protocol_types = (Clock, EventPublisher, MissionStore, TelemetryPort, VehiclePort)

    assert all(protocol_type.__dict__["_is_protocol"] is True for protocol_type in protocol_types)


def test_public_exports_are_stable() -> None:
    assert ports.__all__ == [
        "Clock",
        "EventPublisher",
        "MissionStore",
        "TelemetryPort",
        "VehiclePort",
    ]
