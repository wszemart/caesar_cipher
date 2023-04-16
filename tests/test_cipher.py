from cipher import Rot13, Rot47


class TestCipher:
    def setup_method(self):
        self.rot13 = Rot13()
        self.rot47 = Rot47()

    def test_rot13_encrypt(self):
        text = "Hello, World!"
        assert self.rot13.encrypt(text) == "Uryy|9 d|!yq."

    def test_rot13_decrypt(self):
        text = "Uryy|9 d|!yq."
        assert self.rot13.decrypt(text) == "Hello, World!"

    def test_rot47_encrypt(self):
        text = "Hello, World!"
        assert self.rot47.encrypt(text) == "w6==@[ (@C=5P"

    def test_rot47_decrypt(self):
        text = "w6==@[ (@C=5P"
        assert self.rot47.decrypt(text) == "Hello, World!"
        