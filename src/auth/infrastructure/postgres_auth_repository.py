from sqlalchemy.orm import Session

from src.auth.domain.auth_repository import AuthRepository
from src.auth.infrastructure.auth_user_model import AuthUserModel


class PostgresAuthRepository(AuthRepository):
    def __init__(self, db: Session):
        self.db = db

    def search(self, user_email: str) -> str:
        print(user_email)
        self.db.query(AuthUserModel).filter(AuthUserModel.email == user_email).first()

