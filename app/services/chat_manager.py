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
        user_text: Optional[str],
        vlm_output: Optional[Dict],
    ) -> str:
        """
        Generate a reasoning-aware response using LLM.
        """

        # ---- MOCK LLM IMPLEMENTATION ----
        # Replace later with LLaMA / HF / OpenAI

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
