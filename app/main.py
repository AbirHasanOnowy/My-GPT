from fastapi import FastAPI

app = FastAPI(title="Multimodal Chat AI Service")

@app.get("/health")
async def health_check():
    return {"status": "ok"}
