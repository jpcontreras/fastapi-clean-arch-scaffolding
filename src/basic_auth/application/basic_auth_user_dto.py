from src.auth.domain.auth_provider import AuthProvider


class BasicAuthUserDto:
    def __init__(self, email: str, password: str, first_name: str, last_name: str):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.provider = AuthProvider.email
