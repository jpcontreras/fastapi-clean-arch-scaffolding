from sqlalchemy.orm import Session

from src.auth.application.auth_facebook_user_dto import AuthFacebookUserDto
from src.auth.domain.auth_provider import AuthProvider
from src.auth.domain.auth_repository import AuthRepository
from src.auth.infrastructure.auth_user_model import AuthUserModel
from src.auth.infrastructure.auth_user_profile_model import AuthUserProfileModel


class PostgresAuthRepository(AuthRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def search(self, user_email: str) -> AuthUserModel:
        return self.db_session.query(AuthUserModel).filter(AuthUserModel.email == user_email).first()

    def create(self, user_dto: AuthFacebookUserDto) -> AuthUserModel:
        auth_user = AuthUserModel(uid=user_dto.id, email=user_dto.email, provider=AuthProvider.facebook)
        self.db_session.add(auth_user)
        self.db_session.commit()
        self.db_session.refresh(auth_user)

        auth_user_profile = AuthUserProfileModel(user_id=auth_user.id, first_name=user_dto.first_name,
                                                 last_name=user_dto.last_name, alias_name=user_dto.display_name,
                                                 image_url=user_dto.picture)
        self.db_session.add(auth_user_profile)
        self.db_session.commit()
        return auth_user
