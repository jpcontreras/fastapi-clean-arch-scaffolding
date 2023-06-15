from abc import ABC, abstractmethod


class ITextHasher(ABC):
    @abstractmethod
    def __init__(self, text: str):
        pass

    @abstractmethod
    def hash_text(self) -> str:
        pass

    @abstractmethod
    def verify_text(self, hashed_text: str) -> bool:
        pass
