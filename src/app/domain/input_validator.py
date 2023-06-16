import re

from src.app.infrastructure.i18n.translate import Translate

translate = Translate()


class InputValidator:

    @staticmethod
    def string_value(name: str = 'Field', value: str = '', min_length: int = 0, max_length: int = 0) -> str:
        """Validates a string value
        :param name: (str) Field name
        :param value: (str) Field value
        :param min_length: (int) Minimum length
        :param max_length: (int) Maximum length
        :return: None
        """
        if not value:
            raise ValueError(translate.text('inputs.validation.string.not_empty', name=name))
        if len(value) < min_length or len(value) > max_length:
            raise ValueError(translate.text('inputs.validation.string.length.min_max', name=name, min=min_length, max=max_length))
        return value

    @staticmethod
    def email_value(name: str = 'Field', value: str = '') -> str | ValueError:
        """Validates an email value
        :param name: (str) Field name
        :param value: (str) Field value
        :return: valid email or raises an exception
        """
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, value) is None:
            raise ValueError(translate.text('inputs.validation.email.not_valid', name=name))
        return value

    @staticmethod
    def integer_value(name: str = 'Field', value: int = 0, min_value: int = 0, max_value: int = 0):
        if value < min_value or value > max_value:
            raise ValueError(translate.text('inputs.validation.integer.value_between', name=name, min=min_value, max=max_value))

    @staticmethod
    def boolean_value(name: str = 'Field', value: bool = False):
        if not isinstance(value, bool):
            raise ValueError(translate.text('inputs.validation.boolean.not_valid', name=name))

