from file_handler import *
from typing import Optional
from dataclasses import asdict
from text import *

""" class to handle all logs """
# TODO Text klasa danych.


class MemoryBuffer:
    logs: list = []

    @staticmethod
    def create_log(
        text: str = '',
        rot_type: str = '',
        status: str = '',
        write_to_file: str = '',
        read_from_file: str = '',
    ):
        MemoryBuffer.logs.append(
            Text(text, rot_type, status, write_to_file, read_from_file)
        )

    @staticmethod
    def show_buffer():
        for count, log in enumerate(MemoryBuffer.logs):
            print(f'{count}. {log}')

    @staticmethod
    def clear_buffer():
        MemoryBuffer.logs = []

    @staticmethod
    def del_position():
        choice_to_del = int(input("What do you want to delete? Enter a number: "))
        removed_element = MemoryBuffer.logs.pop(choice_to_del)
        print(f'"{removed_element}" was removed.')

    @staticmethod
    def save_buffer_to_file():
        filename = input("Enter file name to save Memory Buffer: ")
        FileHandler.write_file(filename, MemoryBuffer.logs)


