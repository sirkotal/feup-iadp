import numpy as npy

def matrixMaxMin(file):
    matrix = npy.loadtxt(file, delimiter=';')

    max_value = npy.max(matrix)
    min_value = npy.min(matrix)
    max_position = npy.unravel_index(npy.argmax(matrix),matrix.shape)
    min_position = npy.unravel_index(npy.argmin(matrix),matrix.shape)

    print(f"Max: {max_value}, {max_position}")
    print(f"Min: {min_value}, {min_position}")


file_name = input("Filename:")

matrixMaxMin(file_name)
