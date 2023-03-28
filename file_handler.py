import json

""" class to file handling """


class FileHandler:
    @staticmethod
    def read_file(filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return []

    @staticmethod
    def write_file(filename: str, data, mode="w"):
        if mode == "a":
            current_data = FileHandler.read_file(filename)
            current_data.update(data)
            data = current_data

        with open(filename, mode) as file:
            json.dump(data, file, indent=2)
