import json

""" class to file handling """


class FileHandler:
    def read_file(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return []

    def write_file(self, filename, data, mode="w"):
        if mode == "a":
            current_data = self.read_file(filename)
            current_data.extend(data)
            data = current_data

        with open(filename, mode) as file:
            json.dump(data, file)


test = FileHandler()
# test.read_file('test')
test_data = {"a": 1, "b": 2, "c": 3}
test.write_file("test.json", test_data)
test_data_1 = {"d": 1, "e": 2, "f": 3}
test.write_file("test.json", test_data_1)
test.read_file("test")
