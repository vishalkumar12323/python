# Simple FastAPI

A minimal web API managed with `uv`.

## Run the server

```bash
uv run uvicorn api.main:app --reload
```

The server runs at <http://127.0.0.1:8000>.

## Endpoints

- `GET /` returns `{"message": "Hello, World!"}`.
- `GET /health` returns `{"status": "ok"}`.
- Interactive API documentation is available at <http://127.0.0.1:8000/docs>.