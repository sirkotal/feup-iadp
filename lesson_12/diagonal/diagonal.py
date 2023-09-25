def maxDiagonal(n):
    matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            element = int(input())
            row.append(element)
        matrix.append(row)

    max_abs_values = [0] * n

    for j in range(n):
        max_val = 0
        max_row = -1
        for i in range(j + 1, n):
            abs_val = abs(matrix[i][j])
            if (abs_val > max_val):
                max_val = abs_val
                max_row = i
        max_abs_values[j] = max_row

    for j in range(n):
        max_row = max_abs_values[j]
        if (max_row != -1):
            matrix[j], matrix[max_row] = matrix[max_row], matrix[j]

    return matrix

number = int(input())

final = maxDiagonal(number)

for line in final:
    print("[", end="")
    for i in range(len(line)):
        print("{:.1f}".format(line[i]), end="")
        if (i < len(line) - 1):
            print(", ", end="")
    print("]")