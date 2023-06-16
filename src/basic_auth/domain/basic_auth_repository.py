from abc import ABC, abstractmethod
from src.basic_auth.domain.basic_auth_user_dto import BasicAuthUserDto
from src.basic_auth.infrastructure.basic_auth_user_entity import BasicAuthUserEntity


class BasicAuthRepository(ABC):

    @abstractmethod
    def create(self, user: BasicAuthUserDto) -> BasicAuthUserEntity:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> BasicAuthUserEntity:
        pass
