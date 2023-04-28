from fastapi import Depends
from sqlalchemy.orm import Session
from src.app.infrastructure.db.postgresql_connect import get_db
from src.auth.application.facebook_user_authenticator import FacebookUserAuthenticator
from src.auth.application.validate_user_token import ValidateUserToken
from src.auth.infrastructure.postgres_auth_repository import PostgresAuthRepository


def create_facebook_user_authenticator_depends(db_session: Session = Depends(get_db)):
    return FacebookUserAuthenticator(PostgresAuthRepository(db_session))


def create_validate_user_token_depends(db_session: Session = Depends(get_db)):
    return ValidateUserToken(PostgresAuthRepository(db_session))
