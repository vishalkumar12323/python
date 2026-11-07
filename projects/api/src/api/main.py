from fastapi import FastAPI

app = FastAPI(
    title="API",
    description="A simple web API built with FastAPI",
    version="0.0.1"
)

app.get("/healthz")
def check_health():
    return {"status": "ok", "message": "API status is healthy 🌐"}
