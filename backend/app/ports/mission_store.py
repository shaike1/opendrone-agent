"""Application-owned contract for mission persistence."""

from typing import Protocol

from app.domain import Mission


class MissionStore(Protocol):
    """Define mission persistence operations without choosing storage technology."""

    def save(self, mission: Mission) -> None: ...

    def load(self, mission_id: str) -> Mission | None: ...

    def delete(self, mission_id: str) -> None: ...

    def list(self) -> tuple[Mission, ...]: ...
