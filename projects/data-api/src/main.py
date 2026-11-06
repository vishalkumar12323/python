from fastapi import FastAPI

app = FastAPI(
    title="DataAPI",
    description="Data_api is a simple testing api project build with FastAPI!",
    version="0.0.1"
)

@app.get("/")
def index():
    return {"status": "healthy", "message": "Welcome to DataAPI"}