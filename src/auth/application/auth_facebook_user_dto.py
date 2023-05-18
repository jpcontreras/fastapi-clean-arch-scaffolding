class AuthFacebookUserDto:
    def __init__(self, id: str, email: str, first_name: str, last_name: str, display_name: str, picture: str, provider: str):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.display_name = display_name
        self.picture = picture
        self.provider = provider
