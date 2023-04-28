from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from src.app.infrastructure.settings import Settings
from src.auth.domain.auth_repository import AuthRepository
from src.auth.infrastructure.auth_token_model import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="v1/auth/facebook/login")

settings = Settings()


class ValidateUserToken:
    def __init__(self, auth_repository: AuthRepository):
        self.auth_repository = auth_repository

    def run(self, token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, settings.ACCESS_TOKEN_SECRET_KEY, algorithms=[settings.ACCESS_TOKEN_ALGORITHM])
            user_email: str = payload.get("sub")
            if user_email is None:
                raise credentials_exception
            token_data = TokenData(user_email=user_email)
        except JWTError:
            raise credentials_exception

        auth_user = self.auth_repository.search(token_data.user_email)
        if auth_user is None:
            raise credentials_exception
        return auth_user

