from src.app.domain.input_validator import InputValidator
from src.app.domain.base_dto import BaseDto
from src.auth.domain.auth_provider import AuthProvider
from src.basic_auth.domain.basic_auth_user_provider import BasicAuthUserProvider


class BasicAuthUserDto(BaseDto):
    def __init__(self, email: str, password: str, first_name: str, last_name: str):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.provider = AuthProvider.email.value

    def is_valid(self) -> bool:
        InputValidator.string_value('email', self.email, 1, 255)
        InputValidator.string_value('password', self.password, 10, 50)
        InputValidator.string_value('first_name', self.first_name, 3, 150)
        InputValidator.string_value('last_name', self.last_name, 3, 150)
        BasicAuthUserProvider.is_valid(self.provider)
        return True
