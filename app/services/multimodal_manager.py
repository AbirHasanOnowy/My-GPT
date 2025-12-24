from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import UploadFile

from app.db.models.conversation_log import ConversationLog
from app.services.vlm_manager import VLMManager
from app.services.chat_manager import ChatManager
from app.services.image_storage import save_image


class MultimodalManager:
    """
    Orchestrates text + image → VLM → LLM → DB log
    """

    def __init__(
        self,
        db: Session,
        vlm_model: str = "mock-vlm",
        llm_model: str = "llama-mock",
    ):
        self.db = db
        self.vlm_manager = VLMManager(vlm_model)
        self.chat_manager = ChatManager(llm_model)

    async def handle_request(
        self,
        user_id,
        text: Optional[str],
        images: Optional[List[UploadFile]],
    ) -> ConversationLog:
        """
        Full multimodal pipeline.
        """

        image_paths = []

        # 1️⃣ Save images
        if images:
            for image in images:
                path = await save_image(image)
                image_paths.append(path)

        # 2️⃣ VLM processing
        vlm_output = None
        if image_paths:
            vlm_output = await self.vlm_manager.process_images(image_paths)

        # 3️⃣ LLM reasoning
        response_text = await self.chat_manager.generate_response(
            user_text=text,
            vlm_output=vlm_output,
        )

        # 4️⃣ Persist conversation
        log = ConversationLog(
            user_id=user_id,
            text_query=text,
            image_urls=image_paths or None,
            vlm_output=vlm_output,
            response_text=response_text,
            llm_model_name=self.chat_manager.get_model_name(),
            vlm_model_name=self.vlm_manager.get_model_name(),
        )

        self.db.add(log)
        self.db.commit()
        self.db.refresh(log)

        return log
