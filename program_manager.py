from cipher import Cipher
from file_handler import FileHandler
from program_menu import *


class Manager:
    def __init__(self):
        self.ceasar_cipher = Cipher()
        self.file_handler = FileHandler()
        self.menu = Menu()
        self.__is_running = True
        self.options = {
            1: self.ceasar_cipher.encrypt,
            2: self.ceasar_cipher.decrypt,
            3: self.file_handler.write_file,
            4: self.file_handler.read_file,
            5: self.exit_program
        }

    @staticmethod
    def start():
        return Manager.show_menu()

    @staticmethod
    def show_menu():
        return Menu.show_menu()

    def show_error(self):
        print("Error!")

    def execute(self):
        self.options.get(Menu.get_choice(), self.show_error)()

    def exit_program(self):
        print("Exit the programme")
        self.__is_running = False
