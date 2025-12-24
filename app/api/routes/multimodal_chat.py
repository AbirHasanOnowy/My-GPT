from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.session import get_db
from app.api.deps import get_current_user
from app.db.models.user import User
from app.services.multimodal_manager import MultimodalManager

router = APIRouter()

@router.post("/")
async def multimodal_chat(
    text: Optional[str] = Form(None),
    images: Optional[List[UploadFile]] = File(None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Accept text + optional images, run full multimodal pipeline, return response.
    """

    multimodal_manager = MultimodalManager(db=db)

    # ✅ Call handle_request properly
    log = await multimodal_manager.handle_request(
        user_id=current_user.id,
        text=text,
        images=images
    )

    # Return only needed fields
    return {
        "response_text": log.response_text,
        "vlm_output": log.vlm_output,
        "image_urls": log.image_urls,
        "llm_model": log.llm_model_name,
        "vlm_model": log.vlm_model_name,
        "timestamp": log.timestamp
    }
