from sqlalchemy import Column, UUID, String, Enum, Boolean
from src.common.infrastructure.user_entity import UserEntity


class BasicAuthUserEntity(UserEntity):
    encrypted_password = Column(String, nullable=False)
