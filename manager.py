from typing import Tuple
from cipher import Rot
from buffer import MemoryBuffer
from file_handler import FileHandler
from text import Text


class Manager:
    @staticmethod
    def get_input() -> Tuple[str, str]:
        text = input("Enter text: ")
        rot_type = input("Enter ROT type (rot13/rot47): ")
        return text, rot_type

    @staticmethod
    def encrypt_text():
        text, rot_type = Manager.get_input()
        encrypted_text = Rot.create_rot(rot_type).encrypt(text)
        print("Encrypted text:", encrypted_text)
        MemoryBuffer.create_log(encrypted_text, rot_type=rot_type, status="encrypted")

    @staticmethod
    def decrypt_text():
        text, rot_type = Manager.get_input()
        decrypted_text = Rot.create_rot(rot_type).decrypt(text)
        print("Decrypted text:", decrypted_text)
        MemoryBuffer.create_log(decrypted_text, rot_type=rot_type, status="decrypted")

    @staticmethod
    def read_file():
        filename = input("Enter file name: ")
        loaded_data = FileHandler.read_file(filename)
        print(loaded_data)
        MemoryBuffer.logs = [Text(**txt_dict) for txt_dict in loaded_data]
