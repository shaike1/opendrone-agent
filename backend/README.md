# OpenDrone Agent Backend

This directory contains the FastAPI development status application and the current domain,
application, and port foundation for OpenDrone Agent. Only process health and application version
are wired into the runtime; the other packages provide no drone or mission execution functionality.

## Implemented packages and limits

- `app/domain`: mission, vehicle, and capability entities; state enums; validation exceptions; and
  immutable measurement value objects.
- `app/application/services`: synchronous in-memory construction, association, and descriptive state
  mutation. There is no durability, authorization, safety policy, or execution.
- `app/ports`: `Clock`, `EventPublisher`, `MissionStore`, `TelemetryPort`, and `VehiclePort` Protocol
  contracts. No concrete adapter implements or wires them.
- `app/api`, `app/models`, `app/core`, and `app/main.py`: status routes, response schemas,
  configuration/logging, and FastAPI assembly.

There is no persistence, simulator, external adapter, safety engine, AI/plugin integration, drone
SDK, or hardware access. These absences are authorization boundaries, not an invitation to fill in
the interfaces. Phase 0 remains the only authorized phase; consult the
[roadmap](../docs/ROADMAP.md#authorization-status) before proposing changes.

## Requirements

- Python 3.11 or newer

## Install

Create and activate a virtual environment, then install the application and test dependencies:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[test]'
```

## Run

Start the development server from the `backend` directory:

```bash
uvicorn app.main:app --reload
```

The API is available at `http://127.0.0.1:8000`.
Runtime configuration can be set with these environment variables:

| Variable | Default | Purpose |
| --- | --- | --- |
| `APP_NAME` | `OpenDrone Agent` | Application name returned by `/version` |
| `APP_VERSION` | `0.1.0` | Application version returned by `/version` |
| `LOG_LEVEL` | `INFO` | Python logging level |

Logs are written to standard error as one JSON object per line.

## Endpoints

| Method | Path | Response |
| --- | --- | --- |
| `GET` | `/health` | `{"status": "healthy"}` |
| `GET` | `/version` | `{"name": "OpenDrone Agent", "version": "0.1.0"}` |

Interactive OpenAPI documentation is available at `/docs` while the application is running.

## Test

```bash
pytest
```
