from sqlalchemy import Column, UUID, String, Enum, Boolean
from src.common.infrastructure.user_model import UserModel


class BasicAuthUserModel(UserModel):
    encrypted_password = Column(String, nullable=False)
