class MultimodalManager:
    def __init__(self, vlm_manager, chat_manager):
        self.vlm = vlm_manager
        self.chat = chat_manager

    async def handle(self, text, image_paths):
        vlm_output = None

        if image_paths:
            vlm_output = await self.vlm.process(image_paths)

        response = await self.chat.generate(text, vlm_output)

        return response, vlm_output
