"""Unit tests for application-layer orchestration."""

import pytest
from app.application.services import CapabilityService, MissionService, VehicleService
from app.domain.entities import Capability
from app.domain.enums import CapabilityState, MissionState, VehicleState
from app.domain.exceptions import InvalidEntityError, InvalidMissionStateError
from app.domain.value_objects import BatteryLevel, Position


def test_mission_creation_uses_domain_initial_state() -> None:
    mission = MissionService().create_mission("mission-1", "Survey area")

    assert mission.id == "mission-1"
    assert mission.name == "Survey area"
    assert mission.state is MissionState.CREATED


def test_vehicle_assignment_operates_on_domain_entities() -> None:
    mission = MissionService().create_mission("mission-1", "Survey area")
    vehicle = VehicleService().register_vehicle("vehicle-1", "Simulation vehicle")

    result = MissionService().assign_vehicle(mission, vehicle)

    assert result is mission
    assert mission.assigned_vehicle is vehicle


def test_capability_enable_and_disable() -> None:
    enabled = Capability("survey", "Survey", "Collect survey observations")
    disabled = Capability("mapping", "Mapping", "Create a map", state=CapabilityState.DISABLED)
    service = CapabilityService()

    service.disable(enabled)
    assert enabled.state is CapabilityState.DISABLED

    service.enable(disabled)
    assert disabled.state is CapabilityState.ENABLED


def test_invalid_mission_state_update_is_rejected() -> None:
    mission = MissionService().create_mission("mission-1", "Survey area")

    with pytest.raises(InvalidMissionStateError):
        MissionService().update_state(mission, "ready")  # type: ignore[arg-type]

    assert mission.state is MissionState.CREATED


def test_duplicate_capability_is_rejected() -> None:
    mission = MissionService().create_mission("mission-1", "Survey area")
    capability = Capability("survey", "Survey", "Collect survey observations")
    service = CapabilityService()
    service.attach_to_mission(capability, mission)

    with pytest.raises(InvalidEntityError):
        service.attach_to_mission(capability, mission)

    assert mission.capabilities == (capability,)


def test_vehicle_observations_and_state_are_recorded() -> None:
    service = VehicleService()
    vehicle = service.register_vehicle("vehicle-1", "Simulation vehicle")
    position = Position(10.0, 20.0)
    battery = BatteryLevel(75.0)

    service.update_position(vehicle, position)
    service.update_battery(vehicle, battery)
    service.change_state(vehicle, VehicleState.READY)

    assert vehicle.current_position is position
    assert vehicle.battery_level is battery
    assert vehicle.state is VehicleState.READY
