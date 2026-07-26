"""Unit tests for domain state enumerations."""

from enum import Enum
from typing import TypeVar

import pytest
from app.domain.enums import CapabilityState, MissionState, VehicleState

State = TypeVar("State", bound=Enum)


def test_enum_members_have_stable_string_values() -> None:
    assert MissionState.EXECUTING.value == "executing"
    assert VehicleState.RETURNING.value == "returning"
    assert CapabilityState.DISABLED.value == "disabled"


@pytest.mark.parametrize(
    ("enum_type", "value"),
    [
        (MissionState, "completed"),
        (VehicleState, "emergency"),
        (CapabilityState, "enabled"),
    ],
)
def test_enums_can_be_constructed_from_their_values(enum_type: type[State], value: str) -> None:
    assert enum_type(value).value == value


def test_enum_rejects_unknown_value() -> None:
    with pytest.raises(ValueError):
        MissionState("unknown")
