from abc import ABC, abstractmethod


class BaseDto(ABC):
    @abstractmethod
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass
