import pytest
from fastapi.testclient import TestClient
from main import app


class TestBasicAuthRoutes:
    # @pytest.fixture
    # def test_client(self):
    #     return TestClient(app)
    test_client = TestClient(app)

    def test_post_signup(self):
        # GET /v1/auth/basic/signup
        # Case 1: Should return 422 status code when the request body is empty
        response = self.test_client.post(
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
        response = self.test_client.post(
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
        response = self.test_client.post(
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
        response = self.test_client.post(
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
        response = self.test_client.post(
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
        response = self.test_client.post(
            '/v1/auth/basic/signup',
            json={
                'email': 'test@test.com',
                'password': '1234567890',
                'first_name': 'John',
                'last_name': 'Doe'
            }
        )
        assert response.status_code == 200
        assert response.json()['email'] == 'test@test.com'
        assert response.json()['first_name'] == 'John'
        assert response.json()['last_name'] == 'Doe'
        assert response.json()['provider'] == 'email'
