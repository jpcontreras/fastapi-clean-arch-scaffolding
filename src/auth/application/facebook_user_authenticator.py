from fastapi import HTTPException

from src.auth.application.auth_facebook_user_dto import AuthFacebookUserDto
from src.auth.domain.auth_repository import AuthRepository
# from src.auth.infrastructure.auth_flask_session import create_session


class FacebookUserAuthenticator:
    def __init__(self, auth_repository: AuthRepository):
        self.auth_repository = auth_repository

    def run(self, user: AuthFacebookUserDto):
        auth_user = self.auth_repository.search(user.email)
        if not bool(auth_user):
            auth_user = self.auth_repository.create(user)

        if auth_user.is_blocked:
            raise HTTPException(status_code=401, detail='User Blocked')
        if auth_user.uid == user.id:
            # create_session(user.id)
            pass
        else:
            raise HTTPException(status_code=401, detail='Incorrect login provider')
        return auth_user
