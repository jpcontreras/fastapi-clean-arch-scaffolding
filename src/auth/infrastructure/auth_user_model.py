import uuid
from sqlalchemy import Column, String, Boolean, UUID, Enum
from src.app.infrastructure.db.postgresql_connect import Base
from src.auth.domain.auth_provider import AuthProvider


class AuthUserModel(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True, nullable=False)
    uid = Column(String)
    email = Column(String, unique=True, index=True)
    provider = Column(Enum(AuthProvider))
    is_blocked = Column(Boolean)
