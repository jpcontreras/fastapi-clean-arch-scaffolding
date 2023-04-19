from uuid import UUID

from pydantic import BaseModel

from src.auth.domain.auth_provider import AuthProvider


class AuthUserModel(BaseModel):
    id: UUID
    provider: AuthProvider
    uid: str
    email: str
    is_blocked: bool
