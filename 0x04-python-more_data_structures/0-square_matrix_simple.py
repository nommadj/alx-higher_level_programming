#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    def square(x):
        return x ** 2

    result = list(map(lambda row: list(map(square, row)), matrix))
    return result
