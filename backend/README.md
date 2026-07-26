# OpenDrone Agent Backend

This directory contains the minimal FastAPI foundation for OpenDrone Agent.
It exposes process health and application version information only; it contains no drone or mission functionality.

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
