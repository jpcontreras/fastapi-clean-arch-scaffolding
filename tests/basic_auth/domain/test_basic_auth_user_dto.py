import copy

import pytest
from pydantic import ValidationError

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
        with pytest.raises(ValidationError) as e:
            BasicAuthUserDto(
                email='',
                password='1234567890',
                first_name='John',
                last_name='Doe'
            )
        for error in e.value.errors():
            assert error['msg'] == 'The email value is not a valid email'

        # Case 2: Password field is empty
        with pytest.raises(ValueError) as e:
            BasicAuthUserDto(
                email='test@example.com',
                password='',
                first_name='John',
                last_name='Doe'
            )
        for error in e.value.errors():
            assert error['msg'] == 'The password value cannot be empty'

        # Case 3: First name field is empty
        with pytest.raises(ValueError) as e:
            BasicAuthUserDto(
                email='test@example.com',
                password='1234567890',
                first_name='',
                last_name='Doe'
            )
        for error in e.value.errors():
            assert error['msg'] == 'The first_name value cannot be empty'

        # Case 4: Last name field is empty
        with pytest.raises(ValueError) as e:
            BasicAuthUserDto(
                email='test@example.com',
                password='1234567890',
                first_name='John',
                last_name=''
            )
        for error in e.value.errors():
            assert error['msg'] == 'The last_name value cannot be empty'

        # Case 5: Provider field is empty
        with pytest.raises(ValueError) as e:
            BasicAuthUserDto(
                email='test@example.com',
                password='1234567890',
                first_name='John',
                last_name='Doe',
                provider=''
            )
        for error in e.value.errors():
            assert error['msg'] == 'The provider value cannot be empty'

        # Case 6: Provider is not valid
        with pytest.raises(ValueError) as e:
            BasicAuthUserDto(
                email='test@example.com',
                password='1234567890',
                first_name='John',
                last_name='Doe',
                provider=AuthProvider.facebook.value
            )
        for error in e.value.errors():
            assert error['msg'] == f'Invalid provider value: {AuthProvider.facebook.value}'

        # Case 7: All fields are valid
        assert BasicAuthUserDto(
            email='test@example.com',
            password='1234567890',
            first_name='John',
            last_name='Doe'
        ) == self.auth_user_dto
