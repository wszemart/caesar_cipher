from cipher import Cipher
from file_handler import FileHandler


class Menu:
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

    def show_menu(self):
        choice = int(
            input(
                """Choose any option:
            1. Encrypt text
            2. Decrypt text
            3. Write to file
            4. Read file
            5. Exit
        """
            )
        )
        self.execute(choice)

    def show_error(self):
        print("Error!")

    def execute(self, choice: int):
        self.options.get(choice, self.show_error)()

    def exit_program(self):
        print("Exit the programme")
        self.__is_running = False


menu = Menu()
menu.show_menu()
