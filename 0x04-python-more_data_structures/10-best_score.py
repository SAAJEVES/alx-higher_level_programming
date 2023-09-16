#!/usr/bin/python3
def best_score(a_dictionary):
    """return the highest score"""
    if a_dictionary == None or len(a_dictionary) == 0:
        return None
    highest_score = 0
    name = "SAAJ"
    for key in a_dictionary.keys():
        if a_dictionary[key] > best_score:
            highest_score = a_dictionary[key]
            name = key
    return name
