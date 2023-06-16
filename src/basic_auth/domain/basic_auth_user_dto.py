from typing import Optional
from uuid import UUID
from pydantic import Field, validator
from src.app.domain.input_validator import InputValidator
from src.app.domain.base_dto import BaseDto
from src.auth.domain.auth_provider import AuthProvider
from src.basic_auth.domain.basic_auth_user_provider import BasicAuthUserProvider


class BasicAuthUserDto(BaseDto):
    id: Optional[UUID] = None
    email: str
    password: Optional[str] = None
    first_name: str
    last_name: str
    provider: str = Field(default=AuthProvider.email.value)

    @validator('email')
    def email_is_valid(cls, email) -> str:
        return InputValidator.email_value('email', email)

    @validator('password')
    def password_is_valid(cls, password) -> str:
        return InputValidator.string_value('password', password, 10, 50)

    @validator('first_name')
    def first_name_is_valid(cls, first_name) -> str:
        return InputValidator.string_value('first_name', first_name, 3, 150)

    @validator('last_name')
    def last_name_is_valid(cls, last_name) -> str:
        return InputValidator.string_value('last_name', last_name, 3, 150)

    @validator('provider')
    def provider_is_valid(cls, provider) -> str:
        return BasicAuthUserProvider.is_valid(provider)
