"""Geographic position value object."""

from dataclasses import dataclass
from math import isfinite

from app.domain.exceptions import InvalidPositionError
from app.domain.value_objects.altitude import Altitude


@dataclass(frozen=True, slots=True)
class Position:
    """A WGS 84 geographic position with an optional altitude."""

    latitude_degrees: float
    longitude_degrees: float
    altitude: Altitude | None = None

    def __post_init__(self) -> None:
        """Validate finite latitude and longitude values against geographic bounds."""
        if not isfinite(self.latitude_degrees) or not -90.0 <= self.latitude_degrees <= 90.0:
            raise InvalidPositionError("latitude must be finite and between -90 and 90 degrees")
        if not isfinite(self.longitude_degrees) or not -180.0 <= self.longitude_degrees <= 180.0:
            raise InvalidPositionError("longitude must be finite and between -180 and 180 degrees")
        if self.altitude is not None and not isinstance(self.altitude, Altitude):
            raise InvalidPositionError("altitude must be an Altitude value")
