"""Vehicle application workflows."""

from app.domain.entities import Vehicle
from app.domain.enums import VehicleState
from app.domain.exceptions import InvalidVehicleStateError
from app.domain.value_objects import BatteryLevel, Position


class VehicleService:
    """Coordinate business observations about vehicles without communicating with them."""

    def register_vehicle(self, vehicle_id: str, name: str) -> Vehicle:
        """Create a vehicle in its domain-defined initial state."""
        return Vehicle(id=vehicle_id, name=name)

    def update_position(self, vehicle: Vehicle, position: Position) -> Vehicle:
        """Record a domain position observation."""
        vehicle.current_position = position
        return vehicle

    def update_battery(self, vehicle: Vehicle, battery_level: BatteryLevel) -> Vehicle:
        """Record a domain battery observation."""
        vehicle.battery_level = battery_level
        return vehicle

    def change_state(self, vehicle: Vehicle, state: VehicleState) -> Vehicle:
        """Record a valid descriptive vehicle state."""
        if not isinstance(state, VehicleState):
            raise InvalidVehicleStateError("vehicle state must be a VehicleState")
        vehicle.state = state
        return vehicle
