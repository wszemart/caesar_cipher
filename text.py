from dataclasses import dataclass

""" data class """


@dataclass
class Text:
    text: str
    rot_type:  str
    status: str
    write_to_file: str
    read_from_file: str
