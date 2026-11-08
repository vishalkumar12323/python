# Simple FastAPI

A minimal web API managed with `uv`.

## Run the server

```bash
uv run uvicorn src.main:app --reload
```

The server runs at <http://127.0.0.1:8000>.

## Run with Docker

Build and run the development image with automatic reload:

```bash
docker build --target development -t api:development .
docker run --rm -p 8000:8000 api:development
```

Build and run the production image:

```bash
docker build --target production -t api:production .
docker run --rm -p 8000:8000 api:production
```

## Endpoints

- `GET /healthz` returns `{"status": "ok", "message": "API status is healthy 🌐"}`.
- Interactive API documentation is available at <http://127.0.0.1:8000/docs>.