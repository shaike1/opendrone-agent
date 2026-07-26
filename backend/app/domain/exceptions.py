"""Exceptions raised when core domain invariants are violated."""


class DomainValidationError(ValueError):
    """Base class for invalid values supplied to the domain model."""


class InvalidMissionStateError(DomainValidationError):
    """Raised when a mission is constructed with an unknown state."""


class InvalidVehicleStateError(DomainValidationError):
    """Raised when a vehicle is constructed with an unknown state."""


class InvalidCapabilityStateError(DomainValidationError):
    """Raised when a capability is constructed with an unknown state."""


class InvalidPositionError(DomainValidationError):
    """Raised when geographic coordinates are outside their valid ranges."""


class InvalidAltitudeError(DomainValidationError):
    """Raised when an altitude is not finite."""


class InvalidHeadingError(DomainValidationError):
    """Raised when a heading is outside the normalized compass range."""


class InvalidVelocityError(DomainValidationError):
    """Raised when a velocity is negative or not finite."""


class InvalidBatteryLevelError(DomainValidationError):
    """Raised when a battery percentage is outside zero through one hundred."""


class InvalidEntityError(DomainValidationError):
    """Raised when an entity lacks a required identity or name."""
