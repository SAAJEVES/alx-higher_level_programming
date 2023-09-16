#!/usr/bin/python3
def best_score(a_dictionary):
    """return the highest score"""
    if a_dictionary == None:
        return None
    best_score = 0
    for key in a_dictionary.keys():
        if a_dictionary[key] > best_score:
            best_score = a_dictionary[key]
    return best_score
