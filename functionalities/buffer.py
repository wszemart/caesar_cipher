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
    ) -> None:
        MemoryBuffer.logs.append(Text(text, rot_type, status))

    @staticmethod
    def show_buffer() -> None:
        for count, log in enumerate(MemoryBuffer.logs):
            print(f"{count}. {log}")

    @staticmethod
    def clear_buffer() -> None:
        MemoryBuffer.logs = []

    @staticmethod
    def del_position() -> None:
        if MemoryBuffer.logs:
            choice_to_del: int = int(input("What do you want to delete? Enter a number: "))
            removed_element = MemoryBuffer.logs.pop(choice_to_del)
            print(f'"{removed_element}" was removed.')
        else:
            print("Memory Buffer is empty!")

    @staticmethod
    def save_buffer_to_file() -> None:
        filename: str = str(input("Enter file name to save Memory Buffer: "))
        FileHandler.write_file(filename, [asdict(txt) for txt in MemoryBuffer.logs])
