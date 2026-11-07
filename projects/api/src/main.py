from fastapi import FastAPI
from api.v1.route import v1_routes

app = FastAPI(
    title="API",
    description="A simple web API built with FastAPI",
    version="0.0.1"
)

app.include_router(router=v1_routes, prefix="/api")

@app.get("/healthz")
def check_health() -> dict:
    return {"status": "ok", "message": "API status is healthy 🌐"}
