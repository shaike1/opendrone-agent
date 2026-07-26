"""Application-owned contract for publishing domain events."""

from typing import Protocol


class EventPublisher(Protocol):
    """Publish an event without exposing event-bus or transport details."""

    def publish(self, event: object) -> None: ...
