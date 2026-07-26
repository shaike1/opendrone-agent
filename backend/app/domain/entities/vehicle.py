"""Vehicle entity."""

from dataclasses import dataclass

from app.domain.enums import VehicleState
from app.domain.exceptions import InvalidEntityError, InvalidVehicleStateError
from app.domain.value_objects import BatteryLevel, Position


@dataclass(slots=True)
class Vehicle:
    """A drone represented solely in business terms.

    The entity records current domain information and has no connection or control behavior.
    """

    id: str
    name: str
    state: VehicleState = VehicleState.DISCONNECTED
    battery_level: BatteryLevel | None = None
    current_position: Position | None = None

    def __post_init__(self) -> None:
        """Validate identity and the types of current business observations."""
        if not self.id.strip():
            raise InvalidEntityError("vehicle id must not be blank")
        if not self.name.strip():
            raise InvalidEntityError("vehicle name must not be blank")
        if not isinstance(self.state, VehicleState):
            raise InvalidVehicleStateError("vehicle state must be a VehicleState")
        if self.battery_level is not None and not isinstance(self.battery_level, BatteryLevel):
            raise InvalidEntityError("vehicle battery level must be a BatteryLevel")
        if self.current_position is not None and not isinstance(self.current_position, Position):
            raise InvalidEntityError("vehicle current position must be a Position")
