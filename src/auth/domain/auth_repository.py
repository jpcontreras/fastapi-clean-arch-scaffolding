from abc import ABC, abstractmethod
from src.auth.application.auth_facebook_user_dto import AuthFacebookUserDto
from src.common.infrastructure.user_entity import UserEntity


class AuthRepository(ABC):
    @abstractmethod
    def search(self, user_email: str) -> UserEntity:
        pass

    @abstractmethod
    def create(self, user: AuthFacebookUserDto) -> UserEntity:
        pass
