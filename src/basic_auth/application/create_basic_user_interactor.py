from starlette import status
from src.app.application.base_interactor import BaseInteractor, OutputSuccessContext
from src.app.domain.base_dto import BaseDto
from src.app.domain.i18n.translate_service import TranslateService
from src.basic_auth.domain.basic_auth_user_dto import BasicAuthUserDto
from src.basic_auth.domain.basic_auth_repository import BasicAuthRepository
from src.common.infrastructure.text_hasher import TextHasher


class CreateBasicUserInteractor(BaseInteractor):
    def __init__(self, basic_auth_repository: BasicAuthRepository, translate_service: TranslateService):
        self.basic_auth_repository = basic_auth_repository
        self.translate_service = translate_service

    def process(self, input_dto: BasicAuthUserDto) -> OutputSuccessContext:
        txt_hasher = TextHasher(input_dto.password)
        input_dto.password = txt_hasher.hash_text()
        entity_created = self.basic_auth_repository.create(input_dto)
        output_dto = BasicAuthUserDto(
            id=entity_created.id,
            email=entity_created.email,
            first_name=input_dto.first_name,
            last_name=input_dto.last_name
        )
        return OutputSuccessContext(
            data=[output_dto],
            http_status=status.HTTP_201_CREATED,
            message=self.translate_service.text('entities.user.created')
        )

    def validate(self, input_dto: BaseDto):
        return True
