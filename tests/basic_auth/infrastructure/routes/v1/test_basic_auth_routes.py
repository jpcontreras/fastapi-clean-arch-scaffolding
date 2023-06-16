from starlette import status
from tests.base_integration_test import BaseIntegrationTest, test_client


class TestBasicAuthRoutes(BaseIntegrationTest):

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
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        for error in response.json()['detail']:
            if error['loc'][1] == 'email':
                assert error['msg'] == self.translate.text('inputs.validation.email.not_valid', name='email')
            if error['loc'][1] == 'password':
                assert error['msg'] == self.translate.text('inputs.validation.string.not_empty', name='password')
            if error['loc'][1] == 'first_name':
                assert error['msg'] == self.translate.text('inputs.validation.string.not_empty', name='first_name')
            if error['loc'][1] == 'last_name':
                assert error['msg'] == self.translate.text('inputs.validation.string.not_empty', name='last_name')

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
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        for error in response.json()['detail']:
            if error['loc'][1] == 'email':
                assert error['msg'] == self.translate.text('inputs.validation.email.not_valid', name='email')

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
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        for error in response.json()['detail']:
            if error['loc'][1] == 'password':
                assert error['msg'] == self.translate.text('inputs.validation.string.not_empty', name='password')

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
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        for error in response.json()['detail']:
            if error['loc'][1] == 'first_name':
                assert error['msg'] == self.translate.text('inputs.validation.string.not_empty', name='first_name')

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
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        for error in response.json()['detail']:
            if error['loc'][1] == 'last_name':
                assert error['msg'] == self.translate.text('inputs.validation.string.not_empty', name='last_name')

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
