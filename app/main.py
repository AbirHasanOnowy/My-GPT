from fastapi import FastAPI
from app.api.routes import auth, multimodal_chat



app = FastAPI(title="Multimodal Chat AI Service")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(multimodal_chat.router, prefix="/multimodal-chat",tags=["Multimodal Chat"])

@app.get("/health")
async def health_check():
    return {"status": "ok"}
