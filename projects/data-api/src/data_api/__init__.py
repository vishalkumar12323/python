from fastapi import FastAPI

app = FastAPI(
    title="Data API",
    description="Data_api is a simple testing api project build with FastAPI!",
    version="0.0.1"
)

@app.get("/")
def home():
    return {"status": "healthy", "message": "Welcome"}