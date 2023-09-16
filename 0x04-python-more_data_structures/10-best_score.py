#!/usr/bin/python3
def best_score(a_dictionary):
    """return the highest score"""
    best_score = 0
    name = "SAAJ"
    if a_dictionary == None or len(a_dictionary) == 0:
        return None
    for key in a_dictionary.keys():
        if a_dictionary[key] > best_score:
            best_score = a_dictionary[key]
            name = key
    return name
