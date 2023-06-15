from src.app.domain.input_validator import InputValidator
from src.auth.domain.auth_provider import AuthProvider


class BasicAuthUserProvider:

    @staticmethod
    def is_valid(provider: str) -> str:
        InputValidator.string_value('The provider', provider, 3, 150)
        if provider != AuthProvider.email.value:
            raise ValueError(f'Invalid provider value: {provider}')
        return provider
