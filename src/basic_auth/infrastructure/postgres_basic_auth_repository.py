from sqlalchemy.orm import Session
from src.basic_auth.application.basic_auth_user_dto import BasicAuthUserDto
from src.basic_auth.domain.basic_auth_repository import BasicAuthRepository
from src.basic_auth.infrastructure.basic_auth_user_model import BasicAuthUserModel
from src.common.infrastructure.user_profile_model import UserProfileModel


class PostgresBasicAuthRepository(BasicAuthRepository):

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, user_dto: BasicAuthUserDto) -> BasicAuthUserModel:
        auth_user = BasicAuthUserModel(
            email=user_dto.email, encrypted_password=user_dto.password, provider=user_dto.provider,
        )
        self.db_session.add(auth_user)
        self.db_session.commit()
        self.db_session.refresh(auth_user)

        auth_user_profile = UserProfileModel(
            user_id=auth_user.id, first_name=user_dto.first_name, last_name=user_dto.last_name
        )
        self.db_session.add(auth_user_profile)
        self.db_session.commit()
        return auth_user
