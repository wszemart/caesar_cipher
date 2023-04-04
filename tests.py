import os
from unittest.mock import patch
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
#
#     def test_show_buffer(capsys):
#         MemoryBuffer.create_log(text="probe", rot_type="rot13", status="success")
#         MemoryBuffer.show_buffer()
#         captured = capsys.readouterr()
#         assert "0. Text(text='}!|or', rot_type='rot13', status='encrypted')" in captured.out
#


    # def test_del_position(capsys):
    #     MemoryBuffer.create_log(text="Sample text", rot_type="rot13", status="success")
    #     MemoryBuffer.del_position()
    #     captured = capsys.readouterr()
    #     assert "What do you want to delete?" in captured.out
#
    # def test_save_buffer_to_file(tmpdir):
    #     MemoryBuffer.create_log(text="Sample text", rot_type="rot13", status="success")
    #     filepath = str(tmpdir.join("test_buffer.json"))
    #     MemoryBuffer.save_buffer_to_file(filepath)
    #     assert tmpdir.join("test_buffer.json").check()
