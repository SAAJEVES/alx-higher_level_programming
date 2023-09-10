#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            print("$")
        else:
            i = 0
            for i in range(len(row)):
                if i == len(row) - 1:
                    print("{:d}$".format(row[i]))
                else:
                    print("{:d} ".format(row[i]), end="")
                i += 1
    print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
