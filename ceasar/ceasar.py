def rotate(text, rotation):
    """
    A function to shift the values of the letters from a text by an arbitrary integer.

    Parameters:
        text: The string you wish to encode/decode.
        rotation: The integer value to rotate the text by.

    Example:
    >>> message = "Hello World!"
    >>> encoded = rotate(message, 13)
    >>> print(encoded)
    >>> Output:
    >>> Uryyb Jbeyq!
    """
    result = ""
    if type(text) != str:
        string = str(text)
    else:
        string = text
    for i in range(len(string)):
        char = string[i]
        if char.isalnum():
            if char.isalpha():
                if char.isupper():
                    result += chr((ord(char) + rotation - 65) % 26 + 65)
                else:
                    result += chr((ord(char) + rotation - 97) % 26 + 97)
            elif char.isdigit():
                result += chr((ord(char) + round(rotation /
                                                 26 * 10) - 48) % 10 + 48)
        else:
            result += char
    return result
