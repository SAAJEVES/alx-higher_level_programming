#!/usr/bin/python3
'''function that reads a text file (UTF8) and prints it to stdout'''

def read_file(filename=""):
    '''Reads a Text file and prints it out to the standard Output'''

    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read())
