"""Battery level value object."""

from dataclasses import dataclass
from math import isfinite

from app.domain.exceptions import InvalidBatteryLevelError


@dataclass(frozen=True, slots=True)
class BatteryLevel:
    """A remaining battery charge expressed as a percentage."""

    percent: float

    def __post_init__(self) -> None:
        """Require a finite percentage in the inclusive range zero through one hundred."""
        if not isfinite(self.percent) or not 0.0 <= self.percent <= 100.0:
            raise InvalidBatteryLevelError("battery level must be finite and between 0 and 100")
