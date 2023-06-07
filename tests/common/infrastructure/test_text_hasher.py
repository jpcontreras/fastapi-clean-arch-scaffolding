from src.common.infrastructure.text_hasher import TextHasher


class TestTextHasher:
    text_to_hash = "foo"

    def test_hash_text(self):
        hasher = TextHasher(self.text_to_hash)

        # Case 1: Hash text
        assert hasher.hash_text() is not None

    def test_verify_text(self):
        hasher = TextHasher(self.text_to_hash)
        hashed_text = hasher.hash_text()

        # Case 1: Verify text
        assert hasher.verify_text(hashed_text) is True
