import uuid
from sqlalchemy import Column, UUID, ForeignKey, String
from src.app.infrastructure.db.postgresql_connect import Base


class AuthUserProfileModel(Base):
    __tablename__ = 'user_profiles'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    alias_name = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
