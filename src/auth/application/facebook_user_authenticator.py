from src.auth.application.auth_facebook_user_dto import AuthFacebookUserDto
from src.auth.domain.auth_repository import AuthRepository


class FacebookUserAuthenticator:
    def __init__(self, auth_repository: AuthRepository):
        self.auth_repository = auth_repository

    def run(self, user: AuthFacebookUserDto):
        auth_user = self.auth_repository.search(user.email)
        if not bool(auth_user):
            auth_user = self.auth_repository.create(user)
        # create token auth
        return auth_user
