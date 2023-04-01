from dataclasses import asdict
from file_handler import FileHandler
from text import Text


class MemoryBuffer:
    logs: list[Text] = []

    @staticmethod
    def create_log(
        text: str = "",
        rot_type: str = "",
        status: str = "",
    ):
        MemoryBuffer.logs.append(Text(text, rot_type, status))

    @staticmethod
    def show_buffer():
        for count, log in enumerate(MemoryBuffer.logs):
            print(f"{count}. {log}")

    @staticmethod
    def clear_buffer():
        MemoryBuffer.logs = []

    @staticmethod
    def del_position():
        if MemoryBuffer.logs:
            choice_to_del = int(input("What do you want to delete? Enter a number: "))
            removed_element = MemoryBuffer.logs.pop(choice_to_del)
            print(f'"{removed_element}" was removed.')
        else:
            print("Memory Buffer is empty!")

    @staticmethod
    def save_buffer_to_file():
        filename = input("Enter file name to save Memory Buffer: ")
        FileHandler.write_file(filename, [asdict(txt) for txt in MemoryBuffer.logs])
