from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException
from starlette import status

from src.auth.application.generate_user_token import GenerateUserToken
from src.auth.application.validate_user_token import ValidateUserToken
from src.auth.domain.auth_repository import AuthRepository
from src.auth.infrastructure.auth_user_model import AuthUserModel


class TestValidateUserToken:
    facebook_uuid = '123456'
    auth_user = AuthUserModel(
        id='1',
        uid=facebook_uuid,
        email='test@example.com',
        is_blocked=False,
    )

    def test_run(self):
        # Case 1: When the user email is none in sub attribute of the access token
        generate_user_token = GenerateUserToken()
        self.auth_user.email = None
        access_token = generate_user_token.run(self.auth_user).access_token
        mock_auth_repository = MagicMock(spec=AuthRepository)
        mock_auth_repository.search.return_value = self.auth_user
        validate_user_token = ValidateUserToken(auth_repository=mock_auth_repository)
        with pytest.raises(HTTPException) as e:
            validate_user_token.run(access_token)
        assert str(e.value.detail) == 'Could not validate credentials'
        assert e.value.status_code == status.HTTP_401_UNAUTHORIZED

        # Case 2: When the user not exist in the database
        generate_user_token = GenerateUserToken()
        self.auth_user.email = 'test@example.com'
        access_token = generate_user_token.run(self.auth_user).access_token
        mock_auth_repository = MagicMock(spec=AuthRepository)
        mock_auth_repository.search.return_value = None
        validate_user_token = ValidateUserToken(auth_repository=mock_auth_repository)
        with pytest.raises(HTTPException) as e:
            validate_user_token.run(access_token)
        assert str(e.value.detail) == 'Could not validate credentials'
        assert e.value.status_code == status.HTTP_401_UNAUTHORIZED

        # Case 3: When the access token is valid and user exist in the database
        generate_user_token = GenerateUserToken()
        self.auth_user.email = 'test@example.com'
        access_token = generate_user_token.run(self.auth_user).access_token
        mock_auth_repository = MagicMock(spec=AuthRepository)
        mock_auth_repository.search.return_value = self.auth_user
        validate_user_token = ValidateUserToken(auth_repository=mock_auth_repository)
        result = validate_user_token.run(access_token)
        assert result == self.auth_user

