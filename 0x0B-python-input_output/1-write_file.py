#!/usr/bin/python3

'''function that writes a string to a text file (UTF8) and returns the number of characters written'''
def write_file(filename="", text=""):
    """writes string to a text file and return number of characters

    Args:
        filename: name of file
        text: string to write to the file

    Returns:
        the number of text written to the file
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        num_of_char = file.write(text)
        return num_of_char
