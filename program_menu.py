from manager import Manager

""" class to show menu """


class Menu:
    def __init__(self):
        self.execute = Manager()

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
        self.execute.execute(choice)
