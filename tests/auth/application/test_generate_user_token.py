import time

from src.app.infrastructure.settings import Settings
from src.auth.application.generate_user_token import GenerateUserToken
from jose import jwt
from src.common.infrastructure.user_model import UserModel

settings = Settings()


class TestGenerateUserToken:
    facebook_uuid = '123456'
    auth_user = UserModel(
        id='1',
        uid=facebook_uuid,
        email='test@example.com',
        is_blocked=False,
    )

    def test_run(self):
        generate_user_token = GenerateUserToken()
        result = generate_user_token.run(self.auth_user)

        # Case 1: When the access token is generated successfully
        assert result.access_token is not None

        # Rule 1: The access token must be a string
        assert isinstance(result.access_token, str)

        # Rule 2: The expiration time must be 15 minutes
        decoded_token = jwt.decode(result.access_token, settings.ACCESS_TOKEN_SECRET_KEY, algorithms=[settings.ACCESS_TOKEN_ALGORITHM])
        time_now = time.time()
        seconds_diff = decoded_token['exp'] - time_now
        minutes_diff = round(seconds_diff / 60)
        assert minutes_diff == settings.ACCESS_TOKEN_EXPIRE_MINS
