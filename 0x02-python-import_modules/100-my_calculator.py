#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as m
    import sys

    length = len(sys.argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    if op == '+':
        print("{} {} {} = {}".format(a, op, b, m.add(a, b)))
    elif op == '-':
        print("{} {} {} = {}".format(a, op, b, m.sub(a, b)))
    elif op == '*':
        print("{} {} {} = {}".format(a, op, b, m.mul(a, b)))
    elif op == '/':
        print("{} {} {} = {}".format(a, op, b, m.div(a, b)))
