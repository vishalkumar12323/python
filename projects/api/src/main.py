from fastapi import FastAPI
from api.v1.route import v1_routes
from api.v2.route import v2_routes
from config.database import lifespan

app = FastAPI(
    title="API",
    description="A simple web API built with FastAPI",
    version="1.0.0",
    lifespan=lifespan,
)

api_routes = [v1_routes, v2_routes]

for router in api_routes:
    app.include_router(router=router, prefix="/api")

@app.get("/api/healthz")
def check_health() -> dict:
    return {"status": "ok", "message": "API status is healthy 🌐"}
