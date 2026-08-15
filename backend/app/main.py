from fastapi import FastAPI

app = FastAPI(
    title="ProjectFlow API",
    version="0.1.0",
    description="Project and Task Management System API"
)

@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "ProjectFlow API is Working",
        "version": "0.1.0"
    }

@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "ProjectFlow-API"
    }