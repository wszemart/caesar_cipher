import tempfile
from cipher import Rot13, Rot47
from buffer import MemoryBuffer
from text import Text


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


class TestMemoryBuffer:
    @staticmethod
    def test_create_log():
        MemoryBuffer.create_log(text="Sample text", rot_type="rot13", status="success")
        assert len(MemoryBuffer.logs) == 1
        assert isinstance(MemoryBuffer.logs[0], Text)
        assert MemoryBuffer.logs[0].text == "Sample text"
        assert MemoryBuffer.logs[0].rot_type == "rot13"
        assert MemoryBuffer.logs[0].status == "success"

    @staticmethod
    def test_clear_buffer():
        MemoryBuffer.create_log(text="Sample text", rot_type="rot13", status="success")
        MemoryBuffer.clear_buffer()
        assert len(MemoryBuffer.logs) == 0

    @staticmethod
    def test_del_position():
        MemoryBuffer.create_log(text="Sample text_1", rot_type="rot13", status="success")
        MemoryBuffer.create_log(text="Sample text_2", rot_type="rot47", status="fail")
        len_before_delete = len(MemoryBuffer.logs)
        choice_to_del: int = 1
        MemoryBuffer.logs.pop(choice_to_del)
        len_after_delete = len(MemoryBuffer.logs)
        assert len_before_delete - 1 == len_after_delete
#
    # def test_save_buffer_to_file(tmpdir):
    #     MemoryBuffer.create_log(text="Sample text", rot_type="rot13", status="success")
    #     filepath = str(tmpdir.join("test_buffer.json"))
    #     MemoryBuffer.save_buffer_to_file(filepath)
    #     assert tmpdir.join("test_buffer.json").check()
