"""Mission capability entity."""

from dataclasses import dataclass

from app.domain.enums import CapabilityState
from app.domain.exceptions import InvalidCapabilityStateError, InvalidEntityError


@dataclass(slots=True)
class Capability:
    """A business capability that may be made available to a mission.

    A capability declaration contains no loading, plugin, or execution behavior.
    """

    id: str
    name: str
    description: str
    state: CapabilityState = CapabilityState.ENABLED

    def __post_init__(self) -> None:
        """Validate the capability's identity, display name, and state."""
        if not self.id.strip():
            raise InvalidEntityError("capability id must not be blank")
        if not self.name.strip():
            raise InvalidEntityError("capability name must not be blank")
        if not isinstance(self.state, CapabilityState):
            raise InvalidCapabilityStateError("capability state must be a CapabilityState")

    @property
    def enabled(self) -> bool:
        """Return whether the capability is currently declared as enabled."""
        return self.state is CapabilityState.ENABLED
