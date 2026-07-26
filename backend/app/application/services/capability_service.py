"""Capability application workflows."""

from app.domain.entities import Capability, Mission
from app.domain.enums import CapabilityState
from app.domain.exceptions import InvalidEntityError


class CapabilityService:
    """Coordinate capability declarations without loading or executing implementations."""

    def enable(self, capability: Capability) -> Capability:
        """Mark a capability declaration as enabled."""
        capability.state = CapabilityState.ENABLED
        return capability

    def disable(self, capability: Capability) -> Capability:
        """Mark a capability declaration as disabled."""
        capability.state = CapabilityState.DISABLED
        return capability

    def attach_to_mission(self, capability: Capability, mission: Mission) -> Mission:
        """Attach a capability declaration to a mission once."""
        if any(existing.id == capability.id for existing in mission.capabilities):
            raise InvalidEntityError(f"capability {capability.id!r} is already attached")
        mission.capabilities = (*mission.capabilities, capability)
        return mission

    def detach_from_mission(self, capability: Capability, mission: Mission) -> Mission:
        """Detach a capability declaration from a mission, if present."""
        mission.capabilities = tuple(
            existing for existing in mission.capabilities if existing.id != capability.id
        )
        return mission
