import os

from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):

    FB_CLIENT_ID: str = os.getenv('FB_CLIENT_ID')
    FB_CLIENT_SECRET: str = os.getenv('FB_CLIENT_SECRET')
    FB_REDIRECT_URI: str = os.getenv('FB_REDIRECT_URI')
    DB_URL: str = os.getenv('DB_URL')
    DB_ALEMBIC_URL: str = os.getenv('DB_ALEMBIC_URL')
    ACCESS_TOKEN_EXPIRE_MINS: str = os.getenv('ACCESS_TOKEN_EXPIRE_MINS')
    ACCESS_TOKEN_SECRET_KEY: str = os.getenv('ACCESS_TOKEN_SECRET_KEY')
    ACCESS_TOKEN_ALGORITHM: str = 'HS256'
