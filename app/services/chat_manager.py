class ChatManager:
    def __init__(self):
        pass

    async def generate(self, text: str | None, vlm_output: dict | None) -> str:
        prompt = "You are a multimodal assistant.\n\n"

        if vlm_output:
            prompt += f"Image context:\n{vlm_output}\n\n"

        if text:
            prompt += f"User query:\n{text}\n\n"

        prompt += "Provide a helpful response that reasons about the image."

        # Stage 7 placeholder (LLM later)
        return f"[MOCK RESPONSE]\n{prompt}"
