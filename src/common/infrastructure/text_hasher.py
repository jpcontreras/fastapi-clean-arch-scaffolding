from passlib.context import CryptContext

from src.common.domain.itext_hasher import ITextHasher


class TextHasher(ITextHasher):
    def __init__(self, text: str):
        self.text = text
        self.crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_text(self) -> str:
        return self.crypt_context.hash(self.text)

    def verify_text(self, hashed_text: str) -> bool:
        return self.crypt_context.verify(self.text, hashed_text)
