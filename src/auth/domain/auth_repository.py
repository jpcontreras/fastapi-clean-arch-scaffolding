from abc import ABC, abstractmethod

from src.auth.application.auth_facebook_user_dto import AuthFacebookUserDto
from src.auth.infrastructure.auth_user_model import AuthUserModel


class AuthRepository(ABC):
    @abstractmethod
    def search(self, user_email: str) -> AuthUserModel:
        pass

    @abstractmethod
    def create(self, user: AuthFacebookUserDto) -> AuthUserModel:
        pass
