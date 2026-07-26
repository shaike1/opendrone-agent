.PHONY: up down logs backend frontend clean

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
