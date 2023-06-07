import uuid

from pydantic import BaseModel
from sqlalchemy import Column, UUID, String, Enum, Boolean

from src.auth.domain.auth_provider import AuthProvider


class BasicAuthUserModel(BaseModel):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True, nullable=False)
    email = Column(String, unique=True, index=True)
    provider = Column(Enum(AuthProvider))
    is_blocked = Column(Boolean, default=False)