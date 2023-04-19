from enum import Enum


class AuthProvider(str, Enum):
    facebook = 'facebook'
    google = 'google'
    email = 'email'
