from fastapi import FastAPI
from app.api.routes import auth



app = FastAPI(title="Multimodal Chat AI Service")

app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/health")
async def health_check():
    return {"status": "ok"}
