# Simple FastAPI

A minimal web API managed with `uv`.

## Run the server

```bash
uv run uvicorn src.main:app --reload
```

The server runs at <http://127.0.0.1:8000>.

## Endpoints

- `GET /healthz` returns `{"status": "ok", "message": "API status is healthy 🌐"}`.
- Interactive API documentation is available at <http://127.0.0.1:8000/docs>.