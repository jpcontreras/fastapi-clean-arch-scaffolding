from src.app.application.base_interactor import BaseInteractor
from src.app.domain.base_dto import BaseDto
from src.basic_auth.domain.basic_auth_user_dto import BasicAuthUserDto
from src.basic_auth.domain.basic_auth_repository import BasicAuthRepository
from src.basic_auth.infrastructure.basic_auth_user_entity import BasicAuthUserEntity
from src.common.infrastructure.text_hasher import TextHasher


class CreateBasicUserInteractor(BaseInteractor):
    def __init__(self, basic_auth_repository: BasicAuthRepository):
        self.basic_auth_repository = basic_auth_repository

    def process(self, input_dto: BasicAuthUserDto) -> BasicAuthUserEntity:
        txt_hasher = TextHasher(input_dto.password)
        input_dto.password = txt_hasher.hash_text()
        entity_created = self.basic_auth_repository.create(input_dto)
        return entity_created

    def validate(self, input_dto: BaseDto):
        pass
