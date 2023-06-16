from unittest.mock import MagicMock
from starlette import status
from src.app.infrastructure.i18n.translate import Translate
from src.auth.domain.auth_provider import AuthProvider
from src.basic_auth.application.create_basic_user_interactor import CreateBasicUserInteractor
from src.basic_auth.domain.basic_auth_repository import BasicAuthRepository
from src.basic_auth.domain.basic_auth_user_dto import BasicAuthUserDto
from src.basic_auth.infrastructure.basic_auth_user_entity import BasicAuthUserEntity
from src.common.infrastructure.text_hasher import TextHasher


class TestCreateBasicUserInteractor:
    auth_user_dto = BasicAuthUserDto(
        email='test@example.com',
        password='1234567890',
        first_name='John',
        last_name='Doe'
    )

    def test_run(self):
        mock_auth_repository = MagicMock(spec=BasicAuthRepository)
        translate_service = Translate()

        txt_hasher = TextHasher(self.auth_user_dto.password)
        encrypted_password = txt_hasher.hash_text()

        basic_auth_user_entity = BasicAuthUserEntity()
        basic_auth_user_entity.id = '5364c657-e6a9-4c66-9a09-15a56933af45'
        basic_auth_user_entity.email = self.auth_user_dto.email
        basic_auth_user_entity.first_name = self.auth_user_dto.first_name
        basic_auth_user_entity.last_name = self.auth_user_dto.last_name
        basic_auth_user_entity.encrypted_password = encrypted_password
        basic_auth_user_entity.provider = AuthProvider.email.value
        mock_auth_repository.create.return_value = basic_auth_user_entity
        interactor = CreateBasicUserInteractor(basic_auth_repository=mock_auth_repository,
                                               translate_service=translate_service)

        # Case 1: All fields are valid
        result = interactor.run(self.auth_user_dto)
        assert result.data[0].email == basic_auth_user_entity.email
        assert result.data[0].first_name == basic_auth_user_entity.first_name
        assert result.data[0].last_name == basic_auth_user_entity.last_name
        assert result.http_status == status.HTTP_201_CREATED

        assert result.message == translate_service.text('entities.user.created')

        # Case 2: Verify that the password is encrypted
        result = txt_hasher.verify_text(encrypted_password)
        assert result is True



