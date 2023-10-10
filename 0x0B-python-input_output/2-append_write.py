#!/usr/bin/python3

'''function that appends a string at the end of a text file (UTF8) and returns the number of characters added'''

def append_write(filename="", text=""):
    '''appends a string at the end of a text file

    Args:
        filename: name of text file
        text: string to append to the text file

    Returns:
        number of characters added
    '''
    with open(filename, mode='a', encoding='utf-8') as file:
        num_of_char = file.write(text)
        return num_of_char
