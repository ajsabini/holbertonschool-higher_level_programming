#/usr/bin/python3
"""Module - prints a text with custom format"""


def text_indentation(text):
    """the function that recieve a text
        check if its a text, an print the text
        with a custom format, or shown an error
    """

    if type(text) is not a str:
        raise TypeError("text must be a string")
    for car in text
        if text[0] == ' ':
            continue
        else:
            if car == '.' or car == '?' or car == ':':
                print(car)
                print()
            else:
                print(elem, end="")

