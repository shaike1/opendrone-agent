#!/usr/bin/env bash
# Idempotent Cloud Agent bootstrap for OpenDrone Agent.
# Installs the backend (uv) and frontend (npm) development dependencies.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

# uv manages the backend virtualenv and Python toolchain. Install it once.
if ! command -v uv >/dev/null 2>&1; then
  curl -LsSf https://astral.sh/uv/install.sh | sh
fi
export PATH="$HOME/.local/bin:$PATH"

# The frontend test runner strips TypeScript types natively, which requires
# Node.js >= 22.18. Select the pinned Node 22 line via nvm (matches CI).
export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
# shellcheck disable=SC1091
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
if ! nvm use 22 >/dev/null 2>&1; then
  nvm install 22 >/dev/null
  nvm use 22 >/dev/null
fi

# Non-secret local configuration used by docker-compose based workflows.
if [ ! -f .env ]; then
  cp .env.example .env
fi

# Backend dependencies (creates backend/.venv with dev extras).
(cd backend && uv sync --extra dev)

# Frontend dependencies.
(cd frontend && npm install)

echo "OpenDrone Agent development environment is ready."
