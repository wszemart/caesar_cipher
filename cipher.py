import codecs
from typing import Union

""" class to encrypt and decrypt text on dependency to choose ROT13/ROT47 """


class Cipher:
    ROT13 = 'rot13'
    ROT47 = 'rot47'

    def encrypt(self, text: str, rot_type: str) -> Union[str, None]:
        if rot_type == self.ROT13:
            return codecs.encode(text, 'rot13')
        elif rot_type == self.ROT47:
            encrypted_text: str = ''
            for char in text:
                char_code: int = ord(char)
                if 33 <= char_code <= 126:
                    encrypted_char_code = (char_code + 47 - 33) % 94 + 33
                    encrypted_char = chr(encrypted_char_code)
                    encrypted_text += encrypted_char
                else:
                    encrypted_text += char
            return encrypted_text
        else:
            return None

    def decrypt(self, text: str, rot_type: str) -> Union[str, None]:
        if rot_type == self.ROT13:
            return codecs.encode(text, 'rot13')
        elif rot_type == self.ROT47:
            decrypted_text: str = ''
            for char in text:
                char_code: int = ord(char)
                if 33 <= char_code <= 126:
                    decrypted_char_code: int = (char_code - 47 - 33) % 94 + 33
                    decrypted_char = chr(decrypted_char_code)
                    decrypted_text += decrypted_char
                else:
                    decrypted_text += char
            return decrypted_text
        else:
            return None
