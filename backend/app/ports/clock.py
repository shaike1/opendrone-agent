"""Application-owned contract for obtaining time."""

from datetime import datetime
from typing import Protocol


class Clock(Protocol):
    """Provide the current time through a replaceable, deterministic boundary."""

    def now(self) -> datetime: ...
