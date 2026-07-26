"""Unit tests for domain value objects and their invariants."""

from dataclasses import FrozenInstanceError
from math import inf, nan

import pytest
from app.domain.exceptions import (
    InvalidAltitudeError,
    InvalidBatteryLevelError,
    InvalidHeadingError,
    InvalidPositionError,
    InvalidVelocityError,
)
from app.domain.value_objects import Altitude, BatteryLevel, Heading, Position, Velocity


def test_position_accepts_boundary_coordinates_and_altitude() -> None:
    altitude = Altitude(meters_above_mean_sea_level=-12.5)

    position = Position(latitude_degrees=90.0, longitude_degrees=-180.0, altitude=altitude)

    assert position.altitude == altitude


@pytest.mark.parametrize("latitude", [-90.1, 90.1, inf, nan])
def test_position_rejects_invalid_latitude(latitude: float) -> None:
    with pytest.raises(InvalidPositionError):
        Position(latitude_degrees=latitude, longitude_degrees=0.0)


@pytest.mark.parametrize("longitude", [-180.1, 180.1, inf, nan])
def test_position_rejects_invalid_longitude(longitude: float) -> None:
    with pytest.raises(InvalidPositionError):
        Position(latitude_degrees=0.0, longitude_degrees=longitude)


@pytest.mark.parametrize("percent", [0.0, 37.5, 100.0])
def test_battery_level_accepts_inclusive_percentage_range(percent: float) -> None:
    assert BatteryLevel(percent=percent).percent == percent


@pytest.mark.parametrize("percent", [-0.1, 100.1, inf, nan])
def test_battery_level_rejects_invalid_percentage(percent: float) -> None:
    with pytest.raises(InvalidBatteryLevelError):
        BatteryLevel(percent=percent)


@pytest.mark.parametrize("degrees", [0.0, 180.0, 359.999])
def test_heading_accepts_normalized_degrees(degrees: float) -> None:
    assert Heading(degrees_true=degrees).degrees_true == degrees


@pytest.mark.parametrize("degrees", [-0.1, 360.0, inf, nan])
def test_heading_rejects_degrees_outside_normalized_range(degrees: float) -> None:
    with pytest.raises(InvalidHeadingError):
        Heading(degrees_true=degrees)


@pytest.mark.parametrize("speed", [0.0, 12.25])
def test_velocity_accepts_non_negative_speed(speed: float) -> None:
    assert Velocity(meters_per_second=speed).meters_per_second == speed


@pytest.mark.parametrize("speed", [-0.1, inf, nan])
def test_velocity_rejects_invalid_speed(speed: float) -> None:
    with pytest.raises(InvalidVelocityError):
        Velocity(meters_per_second=speed)


@pytest.mark.parametrize("altitude", [inf, -inf, nan])
def test_altitude_rejects_non_finite_measurement(altitude: float) -> None:
    with pytest.raises(InvalidAltitudeError):
        Altitude(meters_above_mean_sea_level=altitude)


def test_value_objects_are_immutable() -> None:
    battery = BatteryLevel(percent=75.0)

    with pytest.raises(FrozenInstanceError):
        battery.percent = 50.0  # type: ignore[misc]
