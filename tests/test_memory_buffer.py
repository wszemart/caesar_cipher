from buffer import MemoryBuffer
from text import Text
import json
from unittest.mock import patch, mock_open
from unittest import mock
from dataclasses import asdict
import os


class TestMemoryBuffer:
    def test_create_log(self):
        MemoryBuffer.create_log(text="Sample text", rot_type="rot13", status="success")
        assert len(MemoryBuffer.logs) == 1
        assert isinstance(MemoryBuffer.logs[0], Text)
        assert MemoryBuffer.logs[0].text == "Sample text"
        assert MemoryBuffer.logs[0].rot_type == "rot13"
        assert MemoryBuffer.logs[0].status == "success"

    def test_clear_buffer(self):
        MemoryBuffer.create_log(text="Sample text", rot_type="rot13", status="success")
        MemoryBuffer.clear_buffer()
        assert len(MemoryBuffer.logs) == 0

    def test_del_position(self):
        MemoryBuffer.create_log(text="Sample text_1", rot_type="rot13", status="success")
        MemoryBuffer.create_log(text="Sample text_2", rot_type="rot47", status="fail")
        len_before_delete = len(MemoryBuffer.logs)
        with patch('builtins.input', return_value='1'):
            MemoryBuffer.del_position()
        len_after_delete = len(MemoryBuffer.logs)
        assert len_before_delete - 1 == len_after_delete

    def test_save_buffer_to_file(self):
        # MemoryBuffer.create_log(text="Sample text", rot_type="rot13", status="success")
        # log_data = [asdict(txt) for txt in MemoryBuffer.logs]

        with patch('builtins.input', side_effect=['test_file', 'w']):
            with mock.patch('builtins.open', mock_open()) as m:
                print(m.mock_calls)
                MemoryBuffer.create_log(text="Sample text", rot_type="rot13", status="success")
                log_data = [asdict(txt) for txt in MemoryBuffer.logs]
                MemoryBuffer.save_buffer_to_file()
                with open('test_file', 'r') as f:
                    saved_data = json.loads(f.read())
                    print(f'{saved_data} o tu są dane których nie zapisuje!')
                    assert saved_data == log_data

        # with open('C:\\Users\\wszem\\Documents\\mentor\\caesar_cipher\\files\\test_file.json') as file:
        #     data = json.load(file)
        #
        # assert log_data == data
