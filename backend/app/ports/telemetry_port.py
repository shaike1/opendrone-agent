"""Application-owned contract for retrieving vehicle telemetry."""

from typing import Protocol

from app.domain import BatteryLevel, Heading, Position, Vehicle, VehicleState, Velocity


class TelemetryPort(Protocol):
    """Expose telemetry observations using only domain vocabulary."""

    def current_position(self, vehicle: Vehicle) -> Position: ...

    def battery_level(self, vehicle: Vehicle) -> BatteryLevel: ...

    def vehicle_state(self, vehicle: Vehicle) -> VehicleState: ...

    def heading(self, vehicle: Vehicle) -> Heading: ...

    def velocity(self, vehicle: Vehicle) -> Velocity: ...
