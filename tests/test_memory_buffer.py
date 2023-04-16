import tempfile
from buffer import MemoryBuffer
from text import Text
from file_handler import FileHandler
from unittest.mock import patch
import json
import os
import pytest
from unittest.mock import patch, mock_open
from unittest import mock
from dataclasses import asdict


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
        with patch('builtins.input', return_value='1'):
            MemoryBuffer.del_position()
        len_after_delete = len(MemoryBuffer.logs)
        assert len_before_delete - 1 == len_after_delete

    @staticmethod
    def test_save_buffer_to_file():
        MemoryBuffer.create_log(text="Sample text", rot_type="rot13", status="success")
        data = MemoryBuffer.logs[0]

        # read_data = json.dumps({"text": "Sample text", "rot_type": "rot13", "status": "success"})
        # mock_open = mock.mock_open(read_data=read_data)
        data = [asdict(txt) for txt in MemoryBuffer.logs]
        with patch('builtins.input', side_effect=['test_file', 'w']):
            # with mock.patch('builtins.open', mock_open):
            MemoryBuffer.save_buffer_to_file()
            with mock.patch('builtins.open', mock_open):
                with open('files/test_file') as file:
                    data = json.load(file)
        assert {"text": "Sample text", "rot_type": "rot13", "status": "success"} == data
        