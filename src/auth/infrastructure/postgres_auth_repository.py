from sqlalchemy.orm import Session

from src.auth.domain.auth_repository import AuthRepository
from src.auth.infrastructure.auth_user_model import AuthUserModel


class PostgresAuthRepository(AuthRepository):
    def __int__(self, db: Session):
        self.db = db

    @property
    def search(self, user_email: str) -> str:
        self.db.query(AuthUserModel).filter(AuthUserModel.email == user_email).first()

