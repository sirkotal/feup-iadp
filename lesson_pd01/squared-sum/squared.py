import numpy as npy


def squaredSum(start, finish, n):
    array = npy.linspace(initial, final, n)

    squared_array = npy.square(array)

    array_sum = npy.sum(squared_array)

    rounded_sum = round(array_sum, 2)

    print("Sum of the array:", rounded_sum)


initial = int(input("Initial value:"))
final = int(input("Final value:"))
n = int(input("Number of values:"))

squaredSum(initial, final, n)
