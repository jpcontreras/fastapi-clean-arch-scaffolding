from abc import ABC, abstractmethod


class TranslateService(ABC):

    @abstractmethod
    def __init__(self, locale: str):
        pass

    @abstractmethod
    def text(self, text: str) -> str:
        pass
