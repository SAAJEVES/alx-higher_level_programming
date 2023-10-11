#!/usr/bin/python3

'''function that inserts a line of text to a file, 
after each line containing a specific string'''

def append_after(filename="", search_string="", new_string=""):
    '''inserts a line of text to a file after 
    each line containing a specific string

    Args:
        filename: textfile
        search_string: the string to search
        new_string: string to insert
    
    Returns:
        None
    '''
    if search_string == None or new_string == None:
        return
    with open(filename, mode="r", encoding="utf-8") as file:
        words = file.readlines()
        new_words = words[:]

    for i in range(0, len(words)):
        if search_string in words[i]:
            new_words.insert(i + 1, new_string)

    with open(filename, mode="w", encoding="utf-8") as file:
        file.writelines(new_words)
