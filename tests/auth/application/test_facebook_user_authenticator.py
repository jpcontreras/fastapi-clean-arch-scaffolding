import pytest
from fastapi import HTTPException
from unittest.mock import MagicMock
from src.auth.application.auth_facebook_user_dto import AuthFacebookUserDto
from src.auth.application.facebook_user_authenticator import FacebookUserAuthenticator
from src.auth.domain.auth_repository import AuthRepository
from src.common.infrastructure.user_entity import UserEntity


class TestFacebookUserAuthenticator:
    facebook_uuid = '123456'
    user = AuthFacebookUserDto(
        id=facebook_uuid,
        email='test@example.com',
        first_name='John',
        last_name='Doe',
        display_name='John Doe',
        picture='https://example.com/picture.jpg',
        provider='facebook'
    )
    auth_user = UserEntity(
        id='1',
        uid=facebook_uuid,
        email='test@example.com',
        is_blocked=False,
    )

    def test_run(self):
        # Case 1: When the user is not blocked and the uid matches
        mock_auth_repository = MagicMock(spec=AuthRepository)
        mock_auth_repository.search.return_value = self.auth_user
        facebook_authenticator = FacebookUserAuthenticator(auth_repository=mock_auth_repository)
        result = facebook_authenticator.run(self.user)
        assert result == self.auth_user

        # Case 2: When the user is blocked
        self.auth_user.is_blocked = True
        mock_auth_repository.search.return_value = self.auth_user
        facebook_authenticator = FacebookUserAuthenticator(auth_repository=mock_auth_repository)
        with pytest.raises(HTTPException) as e:
            facebook_authenticator.run(self.user)
        assert str(e.value.detail) == 'User Blocked'

        # Case 3: When the user is not blocked but the uid does not match
        self.auth_user.is_blocked = False
        self.auth_user.uid = '654321'
        mock_auth_repository.search.return_value = self.auth_user
        facebook_authenticator = FacebookUserAuthenticator(auth_repository=mock_auth_repository)
        with pytest.raises(HTTPException) as e:
            facebook_authenticator.run(self.user)
        assert str(e.value.detail) == 'Incorrect credentials access'
