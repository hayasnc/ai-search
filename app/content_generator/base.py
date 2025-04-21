from abc import ABC, abstractmethod


class ContentGenerator(ABC):
    @abstractmethod
    def generate_gift_message(
        self, purpose: str, tone: str, audience: str, note: str
    ) -> str:
        pass
