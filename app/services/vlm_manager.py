class VLMManager:
    def __init__(self, strategy):
        self.strategy = strategy

    async def process(self, image_paths: list[str]) -> dict:
        return await self.strategy.analyze(image_paths)
