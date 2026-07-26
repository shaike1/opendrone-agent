# OpenDrone Agent Frontend

The frontend is a small React, Vite, and TypeScript dashboard. It displays the health and version reported by the backend and contains no drone functionality.

## Requirements

- Node.js 20 or newer
- npm 10 or newer
- The OpenDrone Agent backend running at `http://127.0.0.1:8000`

## Installation

```bash
cd frontend
npm install
```

## Running locally

Start the backend as described in [`backend/README.md`](../backend/README.md), then run:

```bash
npm run dev
```

Open the URL printed by Vite (normally `http://localhost:5173`). The Vite development server proxies `/health` and `/version` to the local backend, so no browser CORS configuration is required during development.

## Available scripts

| Command | Purpose |
| --- | --- |
| `npm run dev` | Start the Vite development server with hot reload. |
| `npm run build` | Type-check and create an optimized production build in `dist/`. |
| `npm run typecheck` | Check TypeScript types without creating a build. |
| `npm run preview` | Serve the production build locally for review. |

In production, serve the generated `dist/` directory and route `/health` and `/version` to the backend on the same origin.
