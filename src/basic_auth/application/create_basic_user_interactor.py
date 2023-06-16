from starlette import status
from src.app.application.base_interactor import BaseInteractor, OutputSuccessContext, OutputErrorContext
from src.app.domain.base_dto import BaseDto
from src.app.domain.i18n.translate_service import TranslateService
from src.basic_auth.domain.basic_auth_user_dto import BasicAuthUserDto
from src.basic_auth.domain.basic_auth_repository import BasicAuthRepository
from src.common.infrastructure.text_hasher import TextHasher


class CreateBasicUserInteractor(BaseInteractor):
    def __init__(self, repository: BasicAuthRepository, translate: TranslateService):
        self.repository = repository
        self.translate = translate

    def process(self, input_dto: BasicAuthUserDto) -> OutputSuccessContext | OutputErrorContext:
        user = self.repository.get_by_email(input_dto.email)
        if user:
            return OutputErrorContext(
                http_status=status.HTTP_409_CONFLICT,
                code=self.translate.text('api.errors.email_already_exists.code'),
                message=self.translate.text('api.errors.email_already_exists.message'),
                description=self.translate.text('api.errors.email_already_exists.description')
            )
        txt_hasher = TextHasher(input_dto.password)
        input_dto.password = txt_hasher.hash_text()
        entity_created = self.repository.create(input_dto)
        output_dto = BasicAuthUserDto(
            email=entity_created.email,
            first_name=input_dto.first_name,
            last_name=input_dto.last_name
        )
        return OutputSuccessContext(
            data=[output_dto],
            http_status=status.HTTP_201_CREATED,
            message=self.translate.text('entities.user.created')
        )

    def validate(self, input_dto: BaseDto):
        return True
