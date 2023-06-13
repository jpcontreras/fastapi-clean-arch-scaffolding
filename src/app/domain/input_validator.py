class InputValidator:

    @staticmethod
    def string_value(name: str = 'Field', value: str = '', min_length: int = 0, max_length: int = 0):
        """Validates a string value
        :param name: (str) Field name
        :param value: (str) Field value
        :param min_length: (int) Minimum length
        :param max_length: (int) Maximum length
        :return: None
        """
        if not value:
            raise ValueError(f'{name} value cannot be empty')
        if len(value) < min_length or len(value) > max_length:
            raise ValueError(f'{name} value must be between {min_length} and {max_length} characters')

    @staticmethod
    def integer_value(name: str = 'Field', value: int = 0, min_value: int = 0, max_value: int = 0):
        if value < min_value or value > max_value:
            raise ValueError(f'{name} value must be between {min_value} and {max_value}')

    @staticmethod
    def boolean_value(name: str = 'Field', value: bool = False):
        if not isinstance(value, bool):
            raise ValueError(f'{name} value must be boolean')
