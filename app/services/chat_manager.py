from typing import Dict, Optional


class ChatManager:
    """
    Chat Manager
    Responsible for combining text + VLM output and
    producing an LLM response.
    """

    def __init__(self, model_name: str = "llama-mock"):
        self.model_name = model_name

    async def generate_response(
        self,
        user_text: Optional[str] = None,
        vlm_output: Optional[Dict] = None,
        # chat_history: Optional[list[dict]] = None,
    ) -> str:
        """
        Generate a reasoning-aware response using LLM.
        """

        # ---- MOCK LLM IMPLEMENTATION ----
        # Replace later with LLaMA / HF / OpenAI

        # commented out the previou chat history part 
        # chat_history = chat_history or []
        user_text = user_text or ""

        # for msg in chat_history:
        #     user_text += f"{msg['role'].upper()}: {msg['content']}\n"

        response_parts = []

        if user_text:
            response_parts.append(f"User asked: '{user_text}'.")

        if vlm_output:
            objects = ", ".join(vlm_output.get("objects", []))
            scene = vlm_output.get("scene", "unknown")
            response_parts.append(
                f"The image contains: {objects}. Scene: {scene}."
            )

        response_parts.append(
            "Based on the provided information, this is a mock reasoning response."
        )

        return " ".join(response_parts)

    def get_model_name(self) -> str:
        return self.model_name
