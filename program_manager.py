from cipher import Cipher
from file_handler import FileHandler
from menu import Menu


class Manager:
    def __init__(self):
        self.ceasar_cipher = Cipher()
        self.file_handler = FileHandler()
        self.__is_running = True
        self.options = {
            1: self.ceasar_cipher.encrypt,
            2: self.ceasar_cipher.decrypt,
            3: self.file_handler.write_file,
            4: self.file_handler.read_file,
            5: self.exit_program
        }

    def show_error(self):
        print("Error!")

    def execute(self, choice: int):
        self.options.get(choice, self.show_error)()

    def exit_program(self):
        print("Exit the programme")
        self.__is_running = False


def main():
    menu = Menu()
    menu.show_menu()


if __name__ == '__main__':
    main()
