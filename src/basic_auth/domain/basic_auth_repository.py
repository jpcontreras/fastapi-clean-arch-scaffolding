from abc import ABC, abstractmethod

from src.basic_auth.application.basic_auth_user_dto import BasicAuthUserDto


class BasicAuthRepository(ABC):

    @abstractmethod
    def create(self, user: BasicAuthUserDto):
        pass
