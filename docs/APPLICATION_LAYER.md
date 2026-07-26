# Application Layer

## Responsibilities

The application layer coordinates business workflows using domain entities and value objects.
Its services create domain entities and apply small, synchronous changes to their descriptive state and associations.
They preserve domain validation and return the affected domain entity so callers can continue an in-memory workflow.

The layer depends inward only on `backend/app/domain`.
Its unit tests require no framework, network, device, or external service.

## What belongs here

- Use cases that orchestrate one or more domain entities.
- Business workflows such as creating missions, registering vehicles, and associating capabilities.
- Validation needed to coordinate a workflow, such as preventing duplicate capability identities.
- Transport-neutral DTOs when a future use case needs an application-owned input or output contract.

Capability association and state are declarations only.
They do not grant authority, load code, or execute a capability.
Mission and vehicle state updates record business facts and do not authorize or initiate vehicle activity.

## What does not belong here

- FastAPI, REST, HTTP, or HTTP-specific exceptions.
- Databases, repositories, caches, Redis, or persistence behavior.
- PX4, MAVSDK, vehicle communication, telemetry ingestion, or mission execution.
- Adapters, ports, dependency injection, composition, background jobs, or asynchronous processing.
- Plugin loading, AI SDKs, infrastructure configuration, or framework models.
- Safety-engine behavior or an assertion that descriptive state grants operational authority.

Those concerns require later, separately approved architectural increments and must remain outside these services.
