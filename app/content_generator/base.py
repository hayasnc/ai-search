from abc import ABC, abstractmethod


class ContentGenerator(ABC):
    @abstractmethod
    def generate_content(self, prompt: str) -> str:
        """
        Generate content based on the provided prompt.
        :param prompt: The input prompt for content generation.
        :return: Generated content as a string.
        """
        pass
