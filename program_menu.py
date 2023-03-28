""" class to show menu and get choice from user """


class Menu:
    @staticmethod
    def show_menu():
        print(
            """Choose any option:
            1. Enter text to encrypt
            2. Enter text to decrypt
            3. Enter data to write to file
            4. Read data from file
            5. Show Memory Buffer
            6. Clear Memory Buffer
            7. Delete position from Memory Buffer
            8. Save Memory Buffer to file
            9. Exit
        """
        )

    @staticmethod
    def get_choice():
        choice = int(input("Selected option: "))
        return choice
