from app.services.strategies.vlm.base import BaseVLMStrategy

class MockVLMStrategy(BaseVLMStrategy):

    async def analyze(self, image_paths: list[str]) -> dict:
        return {
            "image_count": len(image_paths),
            "summary": "Images contain general visual content.",
            "objects": ["object1", "object2"],
        }
