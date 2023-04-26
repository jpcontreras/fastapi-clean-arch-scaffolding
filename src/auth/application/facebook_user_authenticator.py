from fastapi import HTTPException
from starlette import status
from src.auth.application.auth_facebook_user_dto import AuthFacebookUserDto
from src.auth.domain.auth_repository import AuthRepository


class FacebookUserAuthenticator:
    def __init__(self, auth_repository: AuthRepository):
        self.auth_repository = auth_repository

    def run(self, user: AuthFacebookUserDto):
        auth_user = self.auth_repository.search(user.email)
        if not bool(auth_user):
            auth_user = self.auth_repository.create(user)

        if auth_user.is_blocked:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='User Blocked'
            )
        if auth_user.uid != user.id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect credentials access",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return auth_user
