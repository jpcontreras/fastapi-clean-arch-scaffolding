from sqlalchemy import Column, String
from src.common.infrastructure.user_entity import UserEntity


class BasicAuthUserEntity(UserEntity):
    encrypted_password = Column(String, nullable=False)
