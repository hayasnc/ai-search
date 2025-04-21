from fastapi import FastAPI

from app.api.v1.endpoints import generate

app = FastAPI(title="AI Message Generator API")

# Include the API router
app.include_router(generate.router, prefix="/api/v1", tags=["AI Message"])
