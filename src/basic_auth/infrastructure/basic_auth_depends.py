from fastapi import Depends
from sqlalchemy.orm import Session
from src.app.infrastructure.db.postgresql_connect import get_db
from src.basic_auth.application.create_basic_user_interactor import CreateBasicUserInteractor
from src.basic_auth.infrastructure.postgres_basic_auth_repository import PostgresBasicAuthRepository


def create_basic_user_depends(db_session: Session = Depends(get_db)):
    return CreateBasicUserInteractor(PostgresBasicAuthRepository(db_session))
