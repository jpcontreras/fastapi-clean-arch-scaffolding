from sqlalchemy.orm import Session

from src.auth.application.auth_facebook_user_dto import AuthFacebookUserDto
from src.auth.domain.auth_provider import AuthProvider
from src.auth.domain.auth_repository import AuthRepository
from src.auth.infrastructure.auth_user_model import AuthUserModel


class PostgresAuthRepository(AuthRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def search(self, user_email: str) -> AuthUserModel:
        print('======> search')
        return self.db_session.query(AuthUserModel).filter(AuthUserModel.email == user_email).first()

    def create(self, user: AuthFacebookUserDto) -> AuthUserModel:
        print('======> create')
        auth_user = AuthUserModel(uid=user.id, email=user.email, provider=AuthProvider.facebook)
        self.db_session.add(auth_user)
        return self.db_session.commit()
