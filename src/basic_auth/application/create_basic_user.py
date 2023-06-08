from src.app.application.interactor_base import InteractorBase
from src.basic_auth.application.basic_auth_user_dto import BasicAuthUserDto
from src.basic_auth.domain.basic_auth_repository import BasicAuthRepository


class CreateBasicUser(InteractorBase):
    def __init__(self, basic_auth_repository: BasicAuthRepository):
        self.basic_auth_repository = basic_auth_repository

    def validate_input_dto(self, input_dto: BasicAuthUserDto):
        pass

    def process(self, input_dto: BasicAuthUserDto):
        pass
