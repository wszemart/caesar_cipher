from typing import Union, Optional
from abc import ABC, abstractmethod

""" class to encrypt and decrypt text on dependency to choose ROT13/ROT47 """


class Rot(ABC):
    ROT13 = "rot13"
    ROT47 = "rot47"

    @abstractmethod
    def encrypt(self, text: str) -> Optional[str]:
        raise NotImplementedError

    @abstractmethod
    def decrypt(self, text: str) -> Optional[str]:
        raise NotImplementedError

    def _apply_rotation(self, char_code: int, rot_value: int) -> int:
        return (char_code + rot_value - 33) % 94 + 33

    @staticmethod
    def create_rot(rot_type: str):
        if rot_type == Rot.ROT13:
            return Rot13()
        elif rot_type == Rot.ROT47:
            return Rot47()


class Rot13(Rot):
    ROT_VALUE = 13

    def encrypt(self, text: str) -> Union[str]:
        return self._apply_rotation_to_text(text, self.ROT_VALUE)

    def decrypt(self, text: str) -> Optional[str]:
        return self._apply_rotation_to_text(text, -self.ROT_VALUE)

    def _apply_rotation_to_text(self, text: str, rot_value: int) -> str:
        result = ""
        for char in text:
            char_code: int = ord(char)
            if 33 <= char_code <= 126:
                encrypted_char_code = self._apply_rotation(char_code, rot_value)
                encrypted_char = chr(encrypted_char_code)
                result += encrypted_char
            else:
                result += char
        return result


class Rot47(Rot):
    ROT_VALUE = 47

    def encrypt(self, text: str) -> Union[str]:
        encrypted_text: str = ""
        for char in text:
            char_code: int = ord(char)
            if 33 <= char_code <= 126:
                encrypted_char_code = (char_code + 47 - 33) % 94 + 33
                encrypted_char = chr(encrypted_char_code)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, text: str) -> Optional[str]:
        return self.encrypt(text)
