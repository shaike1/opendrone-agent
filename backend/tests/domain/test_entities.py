"""Unit tests for construction of domain entities."""

from collections.abc import Callable

import pytest
from app.domain.entities import Capability, Mission, Vehicle
from app.domain.enums import CapabilityState, MissionState, VehicleState
from app.domain.exceptions import InvalidEntityError, InvalidMissionStateError
from app.domain.value_objects import Altitude, BatteryLevel, Position


def test_capability_exposes_enabled_state() -> None:
    enabled = Capability(id="survey", name="Survey", description="Collect survey observations")
    disabled = Capability(
        id="mapping",
        name="Mapping",
        description="Create a map",
        state=CapabilityState.DISABLED,
    )

    assert enabled.enabled is True
    assert disabled.enabled is False


def test_vehicle_construction_uses_domain_value_objects() -> None:
    position = Position(52.52, 13.405, Altitude(34.0))

    vehicle = Vehicle(
        id="vehicle-1",
        name="Simulation Vehicle",
        state=VehicleState.READY,
        battery_level=BatteryLevel(82.0),
        current_position=position,
    )

    assert vehicle.current_position == position
    assert vehicle.battery_level == BatteryLevel(82.0)


def test_mission_construction_associates_capabilities_and_vehicle() -> None:
    capability = Capability("survey", "Survey", "Collect survey observations")
    vehicle = Vehicle("vehicle-1", "Simulation Vehicle", VehicleState.READY)

    mission = Mission(
        id="mission-1",
        name="Example Mission",
        state=MissionState.PLANNED,
        capabilities=(capability,),
        assigned_vehicle=vehicle,
    )

    assert mission.capabilities == (capability,)
    assert mission.assigned_vehicle is vehicle


@pytest.mark.parametrize(
    "entity",
    [
        lambda: Capability(" ", "Survey", "Description"),
        lambda: Vehicle("vehicle-1", " "),
        lambda: Mission("", "Mission"),
    ],
)
def test_entities_reject_blank_identity_or_name(entity: Callable[[], object]) -> None:
    with pytest.raises(InvalidEntityError):
        entity()


def test_mission_rejects_non_domain_state() -> None:
    with pytest.raises(InvalidMissionStateError):
        Mission("mission-1", "Mission", state="planned")  # type: ignore[arg-type]


def test_mission_rejects_non_capability_items() -> None:
    with pytest.raises(InvalidEntityError):
        Mission("mission-1", "Mission", capabilities=("survey",))  # type: ignore[arg-type]
