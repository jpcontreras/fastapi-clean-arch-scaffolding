import copy

import pytest

from src.auth.domain.auth_provider import AuthProvider
from src.basic_auth.domain.basic_auth_user_dto import BasicAuthUserDto


class TestBasicAuthUserDto:
    auth_user_dto = BasicAuthUserDto(
        email='test@example.com',
        password='1234567890',
        first_name='John',
        last_name='Doe'
    )

    def test_validate(self):
        # Case 1: Email field is empty
        auth_user_dto_copy = copy.copy(self.auth_user_dto)
        auth_user_dto_copy.email = None
        with pytest.raises(ValueError) as e:
            auth_user_dto_copy.is_valid()
        assert str(e.value) == 'email value cannot be empty'

        # Case 2: Password field is empty
        auth_user_dto_copy = copy.copy(self.auth_user_dto)
        auth_user_dto_copy.password = None
        with pytest.raises(ValueError) as e:
            auth_user_dto_copy.is_valid()
        assert str(e.value) == 'password value cannot be empty'

        # Case 3: First name field is empty
        auth_user_dto_copy = copy.copy(self.auth_user_dto)
        auth_user_dto_copy.first_name = None
        with pytest.raises(ValueError) as e:
            auth_user_dto_copy.is_valid()
        assert str(e.value) == 'first_name value cannot be empty'

        # Case 4: Last name field is empty
        auth_user_dto_copy = copy.copy(self.auth_user_dto)
        auth_user_dto_copy.last_name = None
        with pytest.raises(ValueError) as e:
            auth_user_dto_copy.is_valid()
        assert str(e.value) == 'last_name value cannot be empty'

        # Case 5: Provider field is empty
        auth_user_dto_copy = copy.copy(self.auth_user_dto)
        auth_user_dto_copy.provider = None
        with pytest.raises(ValueError) as e:
            auth_user_dto_copy.is_valid()
        assert str(e.value) == 'provider value cannot be empty'

        # Case 6: Provider is not valid
        auth_user_dto_copy = copy.copy(self.auth_user_dto)
        auth_user_dto_copy.provider = AuthProvider.facebook.value
        with pytest.raises(ValueError) as e:
            auth_user_dto_copy.is_valid()
        assert str(e.value) == f'Invalid provider value: {AuthProvider.facebook.value}'

        # Case 7: All fields are valid
        assert self.auth_user_dto.is_valid() == True
