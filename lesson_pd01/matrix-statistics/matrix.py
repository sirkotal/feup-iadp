import numpy as npy


def matrixGen(seed, rows, columns):
    seed = 42
    npy.random.seed(seed)

    matrix = npy.random.normal(0, 1, size=(rows, columns))

    return matrix


def matrixStatistics(matrix):
    mean = npy.mean(matrix)
    standard_dev = npy.std(matrix)

    mean = round(mean, 2)
    standard_dev = round(standard_dev, 2)

    print("Mean:", mean, end=", ")
    print("Std:", standard_dev)


s = int(input("Seed:"))
r = int(input("Rows:"))
c = int(input("Columns:"))

new_matrix = matrixGen(s, r, c)

matrixStatistics(new_matrix)
