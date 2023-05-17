import fileinput


class Caesar:
    def __init__(self, text="", rotation=13):
        """
        An object that substitutes letters from a given text by rotating the value by an arbitrary integer.

        Attributes:
            text: The self.text you wish to encode/decode.
            rotation: The integer value to rotate the text by.

        Example:
            >>> caesar = Caesar("Hello World!", 3)
            >>> caesar.rotate()
            >>> print(caesar.text)
            >>> 'Khoor Zruog!'
        """
        self.text = str(text)
        self.rotation = int(rotation)
        self.rotated_text = ""

    def get_text(self):
        return self.text

    def set_text(self, new_text):
        self.text = new_text
        return self.text

    def get_rotation(self):
        return self.rotation

    def set_rotation(self, new_rotation):
        self.rotation = new_rotation
        return self.rotation

    def parse(self, path):
        with fileinput.input(path) as file:
            for line in file:
                self.text += line
        return self.text

    def get_rotated_text(self):
        return self.rotated_text

    def rotate(self):
        result = ""
        for i in range(len(self.text)):
            char = self.text[i]
            if char.isalnum():
                if char.isalpha():
                    if char.isupper():
                        result += chr((ord(char) + self.rotation - 65) %
                                      26 + 65)
                    else:
                        result += chr((ord(char) + self.rotation - 97) %
                                      26 + 97)
                elif char.isdigit():
                    result += chr((ord(char) + round(self.rotation /
                                                     26 * 10) - 48) % 10 + 48)
            else:
                result += char
        self.rotated_text = result
        return self.rotated_text
