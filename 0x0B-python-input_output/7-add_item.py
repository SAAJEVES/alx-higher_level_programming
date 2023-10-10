#!/usr/bin/python3
'''a script that adds all arguments to a Python list, and then save them to a file'''

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def main():
    filename = "add_item.json"

    if (len(sys.argv) == 1 and os.path.isfile(filename) == False):
        save_to_json_file([], filename)
    else:
        python_obj = load_from_json_file(filename)
        new_python_obj = python_obj + sys.argv[1:]
        save_to_json_file(new_python_obj, filename)

if __name__ == "__main__":
    main()
