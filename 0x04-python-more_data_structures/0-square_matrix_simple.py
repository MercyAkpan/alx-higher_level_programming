#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for count in range(len(matrix)):
        new_matrix[count] = list(map(lambda y: y**2, matrix[count]))

    return (new_matrix)
