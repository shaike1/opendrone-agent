"""Mission entity."""

from dataclasses import dataclass, field

from app.domain.entities.capability import Capability
from app.domain.entities.vehicle import Vehicle
from app.domain.enums import MissionState
from app.domain.exceptions import InvalidEntityError, InvalidMissionStateError


@dataclass(slots=True)
class Mission:
    """An operator-defined mission at the business level.

    This entity names the mission, its current state, requested capabilities, and optional vehicle.
    It intentionally provides no planning, transition, validation, or execution behavior.
    """

    id: str
    name: str
    state: MissionState = MissionState.CREATED
    capabilities: tuple[Capability, ...] = field(default_factory=tuple)
    assigned_vehicle: Vehicle | None = None

    def __post_init__(self) -> None:
        """Validate identity and ensure collaborators are domain objects."""
        if not self.id.strip():
            raise InvalidEntityError("mission id must not be blank")
        if not self.name.strip():
            raise InvalidEntityError("mission name must not be blank")
        if not isinstance(self.state, MissionState):
            raise InvalidMissionStateError("mission state must be a MissionState")
        if not isinstance(self.capabilities, tuple) or not all(
            isinstance(capability, Capability) for capability in self.capabilities
        ):
            raise InvalidEntityError("mission capabilities must be a tuple of Capability entities")
        if self.assigned_vehicle is not None and not isinstance(self.assigned_vehicle, Vehicle):
            raise InvalidEntityError("assigned vehicle must be a Vehicle")
