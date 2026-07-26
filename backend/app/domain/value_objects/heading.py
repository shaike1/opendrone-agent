"""Heading value object."""

from dataclasses import dataclass
from math import isfinite

from app.domain.exceptions import InvalidHeadingError


@dataclass(frozen=True, slots=True)
class Heading:
    """A normalized heading in degrees clockwise from true north."""

    degrees_true: float

    def __post_init__(self) -> None:
        """Require a finite heading in the half-open range from zero to 360 degrees."""
        if not isfinite(self.degrees_true) or not 0.0 <= self.degrees_true < 360.0:
            raise InvalidHeadingError(
                "heading must be finite and at least 0 but less than 360 degrees"
            )
