from src.app.domain.input_validator import InputValidator
from src.app.infrastructure.i18n.translate import Translate
from src.auth.domain.auth_provider import AuthProvider

translate = Translate()


class BasicAuthUserProvider:

    @staticmethod
    def is_valid(provider: str) -> str:
        InputValidator.string_value('provider', provider, 3, 150)
        if provider != AuthProvider.email.value:
            raise ValueError(translate.text('entities.user.attributes.provider.not_valid', name='provider'))
        return provider
