#/usr/bin/python3
"""Module - prints a text with custom format"""


def text_indentation(text):
    """the function that recieve a text
        check if its a text, an print the text
        with a custom format, or shown an error
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    if text[0] == ' ':
        space = 1
    else:
        space = 0
    for car in text:
        if car == ' ' and space == 1:
            continue
        else:
            space = 0
            if car == '.' or car == '?' or car == ':':
                print(car)
                print()
                space = 1
            else:
                print(car, end="")

