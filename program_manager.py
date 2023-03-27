from typing import Tuple
from cipher import *
from file_handler import FileHandler
from program_menu import Menu
from buffer import *


class Manager:
    def __init__(self):
        self.file_handler = FileHandler()
        self.menu = Menu()
        self.buffer = MemoryBuffer()
        self.__is_running = True
        self.options = {
            1: self.encrypt_text,
            2: self.decrypt_text,
            3: self.write_file,
            4: self.read_file,
            5: self.buffer.show_buffer,
            6: self.buffer.clear_buffer,
            7: self.buffer.del_position,
            8: self.buffer.save_buffer_to_file,
            9: self.exit_program
        }

    @staticmethod
    def show_menu():
        return Menu.show_menu()

    def execute(self):
        choice = Menu.get_choice()
        if choice in self.options:
            self.options.get(choice)()
        else:
            print("Inccorect choice.")

    def exit_program(self):
        print("Exit the programme")
        self.__is_running = False

    def run(self):
        Manager.show_menu()
        while self.__is_running:
            self.execute()

    def encrypt_text_file(self):
        filename = input("Enter file name: ")
        text = self.file_handler.read_file(filename)
        rot_type = input("Enter ROT type (rot13/rot47): ")
        encrypted_text = Rot.create_rot(rot_type).encrypt(text)
        new_filename = input("Enter new file name to save encrypted text: ")
        self.file_handler.write_file(new_filename, encrypted_text)
        MemoryBuffer.create_log(text, rot_type, status='encrypted')

    def read_file(self, filename):
        filename = input("Enter file name: ")
        data = self.file_handler.read_file(filename)
        print(data)
        MemoryBuffer.create_log(data, read_from_file=filename)

    def write_file(self): #ma przechodzić przez buffer
        filename = input("Enter file name: ")
        data = input("Enter data: ")
        self.file_handler.write_file(filename, data)
        MemoryBuffer.create_log(data, write_to_file=filename)

    def get_input(self) -> Tuple[str, str]:
        text = input("Enter text: ")
        rot_type = input("Enter ROT type (rot13/rot47): ")
        return text, rot_type

    def encrypt_text(self):
        text, rot_type = self.get_input()
        encrypted_text = Rot.create_rot(rot_type).encrypt(text)
        print("Encrypted text:", encrypted_text)
        MemoryBuffer.create_log(text, rot_type, status='encrypted')

    def decrypt_text(self):
        text, rot_type = self.get_input()
        decrypted_text = Rot.create_rot(rot_type).decrypt(text)
        print("Decrypted text:", decrypted_text)
        MemoryBuffer.create_log(text, rot_type, status='decrypted')
