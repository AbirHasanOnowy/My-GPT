from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_user
from app.db.models.conversation_log import ConversationLog
from app.services.image_storage import save_image
from app.services.multimodal_manager import MultimodalManager
from app.services.vlm_manager import VLMManager
from app.services.chat_manager import ChatManager
from app.services.strategies.vlm.mock_vlm import MockVLMStrategy

router = APIRouter()

vlm_manager = VLMManager(MockVLMStrategy())
chat_manager = ChatManager()
multimodal_manager = MultimodalManager(vlm_manager, chat_manager)


@router.post("/")
async def multimodal_chat(
    text: str | None = Form(None),
    images: list[UploadFile] | None = File(None),
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    image_paths = []

    if images:
        for img in images:
            path = await save_image(img)
            image_paths.append(path)

    response, vlm_output = await multimodal_manager.handle(text, image_paths)

    log = ConversationLog(
        user_id=user.id,
        text_query=text,
        image_urls=image_paths or None,
        vlm_output=vlm_output,
        response_text=response,
        llm_model_name="mock-llm",
        vlm_model_name="mock-vlm",
    )

    db.add(log)
    db.commit()

    return {"response": response}
