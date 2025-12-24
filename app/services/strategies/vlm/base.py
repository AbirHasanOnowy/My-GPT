from abc import ABC, abstractmethod

class BaseVLMStrategy(ABC):

    @abstractmethod
    async def analyze(self, image_paths: list[str]) -> dict:
        """
        Returns structured image understanding
        """
        pass
