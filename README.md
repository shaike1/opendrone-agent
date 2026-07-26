# OpenDrone Agent

OpenDrone Agent is an open, safety-first platform for building auditable agent-assisted drone
operations. The current application foundation consists of a FastAPI backend and a React frontend.
This development stack provides only the local web application environment; it does not include
drone integrations or operational functionality.

## Prerequisites

The recommended local workflow requires:

- [Docker](https://docs.docker.com/engine/install/) with Docker Compose v2; and
- `make` (optional, because every Make target is a short wrapper around `docker compose`).

No local Python or Node.js installation is needed when using Docker Compose.

The local quality workflow additionally requires Python 3.11 or newer, [uv](https://docs.astral.sh/uv/),
Node.js with npm, and optionally [pre-commit](https://pre-commit.com/).

## Local setup

Create the local environment file from the non-secret template:

```sh
cp .env.example .env
```

The defaults expose the backend at `http://localhost:8000` and the frontend at
`http://localhost:5173`. Edit `.env` to change the application metadata, log level, or host ports.
The local `.env` file is ignored by Git and must not contain committed credentials.

## Start the stack

Build the development images and start both services:

```sh
make up
```

Docker Compose bind-mounts both source directories. Uvicorn reloads backend changes, and Vite
provides hot module replacement for frontend changes. Press `Ctrl+C` to leave the attached process,
or use `make logs` to follow output after starting Compose separately.

To work on one service at a time, use `make backend` or `make frontend`. The frontend target also
starts the backend because the frontend service depends on it.

If `make` is unavailable, run the equivalent command directly:

```sh
docker compose up --build
```

## Developer quality workflow

Install the backend and frontend development dependencies:

```sh
cd backend && uv sync --extra dev
cd ../frontend && npm install
cd ..
```

Run all static analysis, formatting checks, and tests from the repository root:

```sh
make lint
make test
```

`make lint` runs Ruff, MyPy, ESLint, and Prettier in check mode. `make test` runs the backend pytest
suite and the frontend TypeScript check. Apply the configured formatters with:

```sh
make format
```

To run the same formatting and linting checks automatically before each commit, install the hooks:

```sh
pre-commit install
pre-commit run --all-files
```

Hook installation changes only the local Git checkout. The repository does not include CI/CD
configuration at this stage.

## Stop and clean up

Stop and remove the development containers and network:

```sh
make down
```

To also remove the Compose-managed frontend dependency volume and orphaned containers, run:

```sh
make clean
```

The cleanup command does not delete source files or local images.

## Environment variables

| Variable | Default | Purpose |
| --- | --- | --- |
| `APP_NAME` | `OpenDrone Agent` | Backend application name |
| `APP_VERSION` | `0.1.0` | Backend version exposed by the API |
| `LOG_LEVEL` | `INFO` | Backend logging level |
| `BACKEND_PORT` | `8000` | Backend port exposed on the host |
| `FRONTEND_PORT` | `5173` | Frontend port exposed on the host |

## Project structure

```text
.
├── backend/                 # FastAPI application, tests, and development image
│   ├── app/                 # Backend source
│   ├── tests/               # Backend tests
│   ├── Dockerfile
│   └── pyproject.toml
├── frontend/                # React/Vite application and development image
│   ├── src/                 # Frontend source
│   ├── Dockerfile
│   └── package.json
├── docs/                    # Architecture, roadmap, and contributor documentation
├── .env.example             # Safe local configuration template
├── docker-compose.yml       # Local backend/frontend orchestration
└── Makefile                 # Local development command shortcuts
```

## Project documentation

- [Project charter](PROJECT.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Roadmap](docs/ROADMAP.md)
- [Contributing](docs/CONTRIBUTING.md)
- [AI development context](AI_CONTEXT.md)

## License and security

Licensing, disclosure channels, and a security policy will be selected before accepting executable
code. Until then, do not report sensitive operational or vulnerability details in public issues.
