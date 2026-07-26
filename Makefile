.PHONY: up down logs backend frontend clean lint format test

up:
	docker compose up --build

down:
	docker compose down

logs:
	docker compose logs --follow

backend:
	docker compose up --build backend

frontend:
	docker compose up --build frontend

clean:
	docker compose down --volumes --remove-orphans

lint:
	cd backend && uv run --extra dev ruff check app tests
	cd backend && uv run --extra dev mypy app tests
	cd frontend && npm run lint
	cd frontend && npm run format:check

format:
	cd backend && uv run --extra dev ruff check --fix app tests
	cd backend && uv run --extra dev ruff format app tests
	cd frontend && npm run format

test:
	cd backend && uv run --extra dev pytest
	cd frontend && npm test
