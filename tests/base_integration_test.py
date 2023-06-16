import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from main import app
from src.app.infrastructure.db.postgresql_connect import get_db
from src.app.infrastructure.i18n.translate import Translate
from src.common.infrastructure.user_entity import UserEntity
from src.common.infrastructure.user_profile_entity import UserProfileEntity

DB_URL = f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@db:5432/{os.getenv('POSTGRES_DB')}"
engine = create_engine(DB_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
test_client = TestClient(app)


class BaseIntegrationTest:
    translate = Translate()

    def setup_method(self, module):
        session = TestingSessionLocal()
        session.query(UserProfileEntity).delete()
        session.commit()
        session.query(UserEntity).delete()
        session.commit()
