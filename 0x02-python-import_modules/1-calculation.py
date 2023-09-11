#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as m
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, m.add(a, b)))
    print("{} - {} = {}".format(a, b, m.sub(a, b)))
    print("{} * {} = {}".format(a, b, m.mul(a, b)))
    print("{} / {} = {}".format(a, b, m.div(a, b)))
