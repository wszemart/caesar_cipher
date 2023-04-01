from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem, SubmenuItem
from manager import Manager
from buffer import MemoryBuffer


class Menu:
    @staticmethod
    def core_menu():
        menu = ConsoleMenu("Cipher Menu")

        encrypt = FunctionItem("Encrypt", Manager.encrypt_text)
        decrypt = FunctionItem("Decrypt", Manager.decrypt_text)
        read_file = FunctionItem("Read data from file", Manager.read_file)
        menu.append_item(encrypt)
        menu.append_item(decrypt)
        menu.append_item(read_file)
        return menu

    @staticmethod
    def sub_menu():
        submenu = ConsoleMenu("Memory Buffer Menu")
        show_buffer = FunctionItem("Show buffer", MemoryBuffer.show_buffer)
        clear_buffer = FunctionItem("Clear buffer", MemoryBuffer.clear_buffer)
        delete_position = FunctionItem(
            "Delete position from Memory Buffer", MemoryBuffer.del_position
        )
        save_buffer = FunctionItem("Save Buffer to file", MemoryBuffer.save_buffer_to_file)

        submenu.append_item(show_buffer)
        submenu.append_item(clear_buffer)
        submenu.append_item(delete_position)
        submenu.append_item(save_buffer)
        submenu = SubmenuItem("Memory Buffer Menu", submenu=submenu)
        return submenu

    @staticmethod
    def connect_menu_sub_menu(menu, submenu):
        menu.append_item(submenu)
        submenu.set_menu(menu)

    @staticmethod
    def start_menu():
        menu = Menu.core_menu()
        sub_menu = Menu.sub_menu()
        Menu.connect_menu_sub_menu(menu, sub_menu)
        menu.start()
        menu.join()
