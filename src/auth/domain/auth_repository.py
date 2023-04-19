from abc import ABC, abstractmethod


class AuthRepository(ABC):
    @abstractmethod
    def search(self, user_email: str) -> str:
        pass
