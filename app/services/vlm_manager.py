from typing import List, Dict
from pathlib import Path


class VLMManager:
    """
    Vision-Language Model Manager
    Responsible for converting images into structured information
    usable by an LLM for reasoning.
    """

    def __init__(self, model_name: str = "mock-vlm"):
        self.model_name = model_name

    async def process_images(self, image_paths: List[str]) -> Dict:
        """
        Takes image file paths and returns structured semantic information.
        """

        # ---- MOCK IMPLEMENTATION ----
        # Replace this later with BLIP-2 / LLaVA / HF VLM

        objects = []
        for path in image_paths:
            filename = Path(path).name.lower()
            if "cat" in filename:
                objects.append("cat")
            elif "dog" in filename:
                objects.append("dog")
            else:
                objects.append("unknown_object")

        return {
            "objects": list(set(objects)),
            "scene": "unknown_scene",
            "attributes": ["mocked"],
            "summary": f"{len(image_paths)} image(s) processed by VLM",
        }

    def get_model_name(self) -> str:
        return self.model_name
