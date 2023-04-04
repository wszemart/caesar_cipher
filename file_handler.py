from typing import Union, List, Dict
import json


class FileHandler:
    @staticmethod
    def read_file(filename) -> Union[List, Dict]:
        try:
            with open(f"files/{filename}.json", "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return []

    @staticmethod
    def write_file(filename: str, data) -> None:
        mode: str = input("Choose mode to write file (w/a): ")
        if mode == "a":
            current_data: Union[list, dict] = FileHandler.read_file(filename)
            current_data.append(data)
            data = current_data

        with open(f"files/{filename}.json", mode) as file:
            json.dump(data, file, indent=2)
