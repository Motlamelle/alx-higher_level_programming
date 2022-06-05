#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        i = 0
        ln = len(row)-1
        for col in row:
            if i < ln:
                print("{:d} ".format(col), end="")
                i=i+1
            else:
                print("{:d}".format(col), end="")
        print("")
