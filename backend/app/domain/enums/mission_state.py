"""Mission lifecycle states."""

from enum import StrEnum


class MissionState(StrEnum):
    """A business-level stage in a mission's lifecycle.

    The enum describes state only; it deliberately does not define transitions or execution.
    """

    CREATED = "created"
    PLANNED = "planned"
    VALIDATED = "validated"
    READY = "ready"
    EXECUTING = "executing"
    PAUSED = "paused"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
