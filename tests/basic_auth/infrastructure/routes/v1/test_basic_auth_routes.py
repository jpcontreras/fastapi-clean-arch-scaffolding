from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette import status
from main import app
from src.app.infrastructure.db.postgresql_connect import get_db
from src.common.infrastructure.user_entity import UserEntity
from src.common.infrastructure.user_profile_entity import UserProfileEntity
import os

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


def setup_module(module):
    session = TestingSessionLocal()
    session.query(UserProfileEntity).delete()
    session.commit()
    session.query(UserEntity).delete()
    session.commit()


class TestBasicAuthRoutes:

    def test_post_signup(self):
        # GET /v1/auth/basic/signup
        # Case 1: Should return 422 status code when the request body is empty
        response = test_client.post(
            '/v1/auth/basic/signup',
            json={
                'email': '',
                'password': '',
                'first_name': '',
                'last_name': ''
            }
        )
        assert response.status_code == 422
        for error in response.json()['detail']:
            if error['loc'][1] == 'email':
                assert error['msg'] == 'The email value is not a valid email'
            if error['loc'][1] == 'password':
                assert error['msg'] == 'The password value cannot be empty'
            if error['loc'][1] == 'first_name':
                assert error['msg'] == 'The first_name value cannot be empty'
            if error['loc'][1] == 'last_name':
                assert error['msg'] == 'The last_name value cannot be empty'

        # Case 2: Should return 422 status code when the email field is invalid
        response = test_client.post(
            '/v1/auth/basic/signup',
            json={
                'email': 'test',
                'password': '1234567890',
                'first_name': 'John',
                'last_name': 'Doe'
            }
        )
        assert response.status_code == 422
        for error in response.json()['detail']:
            if error['loc'][1] == 'email':
                assert error['msg'] == 'The email value is not a valid email'

        # Case 3: Should return 422 status code when the password field is invalid
        response = test_client.post(
            '/v1/auth/basic/signup',
            json={
                'email': 'test@test.com',
                'password': '',
                'first_name': 'John',
                'last_name': 'Doe'
            }
        )
        assert response.status_code == 422
        for error in response.json()['detail']:
            if error['loc'][1] == 'password':
                assert error['msg'] == 'The password value cannot be empty'

        # Case 4: Should return 422 status code when the first_name field is invalid
        response = test_client.post(
            '/v1/auth/basic/signup',
            json={
                'email': 'test@test.com',
                'password': '1234567890',
                'first_name': '',
                'last_name': 'Doe'
            }
        )
        assert response.status_code == 422
        for error in response.json()['detail']:
            if error['loc'][1] == 'first_name':
                assert error['msg'] == 'The first_name value cannot be empty'

        # Case 5: Should return 422 status code when the last_name field is invalid
        response = test_client.post(
            '/v1/auth/basic/signup',
            json={
                'email': 'test@test.com',
                'password': '1234567890',
                'first_name': 'John',
                'last_name': ''
            }
        )
        assert response.status_code == 422
        for error in response.json()['detail']:
            if error['loc'][1] == 'last_name':
                assert error['msg'] == 'The last_name value cannot be empty'

        # Case 6: Should return 201 status code when the request body is valid
        response = test_client.post(
            '/v1/auth/basic/signup',
            json={
                'email': 'test@test.com',
                'password': '1234567890',
                'first_name': 'John',
                'last_name': 'Doe'
            }
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()['data'][0]['email'] == 'test@test.com'
        assert response.json()['data'][0]['first_name'] == 'John'
        assert response.json()['data'][0]['last_name'] == 'Doe'
        assert response.json()['data'][0]['provider'] == 'email'
