from src.auth.application.auth_facebook_user_dto import AuthFacebookUserDto
from src.auth.domain.auth_repository import AuthRepository


class FacebookUserAuthenticator:
    def __init__(self, auth_repository: AuthRepository):
        self.auth_repository = auth_repository

    def run(self, user: AuthFacebookUserDto):
        print('---------------  ----------------')
        # print(user)
        self.auth_repository.search(user.email)
