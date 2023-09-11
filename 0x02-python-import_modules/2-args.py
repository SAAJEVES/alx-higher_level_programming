#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print("{} arguments.".format(len(sys.argv) - 1))
elif len(sys.argv) == 2:
    i = 1
    a = sys.argv
    a.pop(0)
    print("{} argument.".format(len(sys.argv)))
    print("{}: {}".format(i, a[0]))
else:
    i = 1
    a = sys.argv
    a.pop(0)
    print("{} arguments.".format(len(sys.argv)))
    for val in a:
        print("{:d}: {:s}".format(i, val))
        i += 1
