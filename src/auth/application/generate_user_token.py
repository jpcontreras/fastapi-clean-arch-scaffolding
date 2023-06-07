from datetime import timedelta, datetime
from typing import Optional
from jose import jwt
from src.app.infrastructure.settings import Settings
from src.auth.infrastructure.auth_token_model import Token
from src.common.infrastructure.user_model import UserModel

settings = Settings()


class GenerateUserToken:
    def run(self, auth_user: UserModel) -> Token:
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINS)
        access_token = self._create_access_token(
            data={"sub": auth_user.email}, expires_delta=access_token_expires
        )
        return Token(access_token=access_token, token_type="bearer")

    def _create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, settings.ACCESS_TOKEN_SECRET_KEY, algorithm=settings.ACCESS_TOKEN_ALGORITHM)
