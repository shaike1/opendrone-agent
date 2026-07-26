"""Velocity value object."""

from dataclasses import dataclass
from math import isfinite

from app.domain.exceptions import InvalidVelocityError


@dataclass(frozen=True, slots=True)
class Velocity:
    """A non-negative scalar speed in metres per second."""

    meters_per_second: float

    def __post_init__(self) -> None:
        """Reject negative and non-finite speed measurements."""
        if not isfinite(self.meters_per_second) or self.meters_per_second < 0.0:
            raise InvalidVelocityError("velocity must be finite and non-negative")
