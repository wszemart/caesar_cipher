""" class to show menu and get choice from user """


class Menu:
    @staticmethod
    def show_menu():
        print(
                """Choose any option:
            1. Encrypt text
            2. Decrypt text
            3. Write to file
            4. Read from file
            5. Exit
        """
            )

    @staticmethod
    def get_choice():
        choice = int(input())
        return choice
