import os
import uuid
from fastapi import UploadFile
from app.core.config import settings

UPLOAD_DIR = settings.UPLOAD_DIR

os.makedirs(UPLOAD_DIR, exist_ok=True)

async def save_image(file: UploadFile) -> str:
    ext = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    path = os.path.join(UPLOAD_DIR, filename)

    with open(path, "wb") as f:
        f.write(await file.read())

    return path
