"""Altitude value object."""

from dataclasses import dataclass
from math import isfinite

from app.domain.exceptions import InvalidAltitudeError


@dataclass(frozen=True, slots=True)
class Altitude:
    """An altitude in metres above mean sea level.

    Negative values are valid for locations below mean sea level. Infinite and NaN values are not.
    """

    meters_above_mean_sea_level: float

    def __post_init__(self) -> None:
        """Ensure the altitude is a finite measurement."""
        if not isfinite(self.meters_above_mean_sea_level):
            raise InvalidAltitudeError("altitude must be finite")
