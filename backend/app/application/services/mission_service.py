"""Mission application workflows."""

from app.domain.entities import Capability, Mission, Vehicle
from app.domain.enums import MissionState
from app.domain.exceptions import InvalidEntityError, InvalidMissionStateError


class MissionService:
    """Coordinate changes to mission domain entities without persistence or execution."""

    def create_mission(self, mission_id: str, name: str) -> Mission:
        """Create a mission in its domain-defined initial state."""
        return Mission(id=mission_id, name=name)

    def assign_vehicle(self, mission: Mission, vehicle: Vehicle) -> Mission:
        """Associate a domain vehicle with a mission."""
        mission.assigned_vehicle = vehicle
        return mission

    def add_capability(self, mission: Mission, capability: Capability) -> Mission:
        """Associate a capability, rejecting duplicate capability identities."""
        if any(existing.id == capability.id for existing in mission.capabilities):
            raise InvalidEntityError(f"capability {capability.id!r} is already attached")
        mission.capabilities = (*mission.capabilities, capability)
        return mission

    def remove_capability(self, mission: Mission, capability: Capability) -> Mission:
        """Remove the capability with the supplied domain identity, if present."""
        mission.capabilities = tuple(
            existing for existing in mission.capabilities if existing.id != capability.id
        )
        return mission

    def update_state(self, mission: Mission, state: MissionState) -> Mission:
        """Record a valid descriptive mission state."""
        if not isinstance(state, MissionState):
            raise InvalidMissionStateError("mission state must be a MissionState")
        mission.state = state
        return mission
