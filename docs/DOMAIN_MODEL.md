# Domain Model

## Purpose

The OpenDrone Agent domain model provides a shared business vocabulary for describing missions,
vehicles, capabilities, and their measurements.

It describes facts and concepts only.
It does not authorize, plan, validate, or execute drone operations.

## Mission

A **Mission** identifies an operator-defined objective by its identifier and name.
It records a lifecycle state, the capabilities relevant to the objective, and an optional assigned
vehicle.

Mission states distinguish creation, planning, validation, readiness, execution, pausing, and final
outcomes.
They are descriptive and do not themselves permit a transition or confer authority to act.

## Vehicle

A **Vehicle** represents a drone as a business concept.
It has an identifier, a name, and a state describing its current availability or activity.
When known, its remaining battery level and current geographic position may be recorded.

A vehicle does not expose a connection, protocol, command, or vendor-specific concept.

## Capability

A **Capability** names and describes an ability that can be associated with a mission.
Its state records whether the capability is enabled or disabled.

Capability membership is a declaration only.
It does not load code, grant permission, or make the capability executable.

## Value objects

Value objects express measurements with explicit units and lightweight invariants:

- **Position** is a WGS 84 latitude and longitude with an optional altitude.
- **Altitude** is measured in metres above mean sea level and may be negative.
- **Heading** is measured clockwise in degrees from true north and is normalized from zero up to,
  but not including, 360 degrees.
- **Velocity** is a non-negative scalar speed measured in metres per second.
- **BatteryLevel** is a remaining-charge percentage from zero through one hundred.

These concepts are immutable.
Invalid coordinates, percentages, normalized headings, and non-finite measurements are rejected so
that invalid observations cannot silently enter the domain vocabulary.

## Domain boundaries

The domain is pure Python and sits at the innermost architectural boundary.
It has no dependency on web frameworks, validation frameworks, persistence, transports, caches,
vehicle SDKs, AI SDKs, deployment systems, or external services.

The model does not include application orchestration, repositories, APIs, dependency injection,
plugin loading, safety policy, or mission execution.
Outer layers may translate their data into domain concepts, but outer-layer representations and
behavior do not belong in this model.
