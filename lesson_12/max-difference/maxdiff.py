def maxDiffConseq(n):
    matrix = []
    max_diff = 0
    temp = 0

    for i in range(n):
        row = []
        for j in range(n):
            element = int(input())
            row.append(element)
        matrix.append(row)

    for line in (matrix):
        for i in range(n):
            max_diff = max(max_diff, abs(line[i] - temp))
            temp = line[i]

    return max_diff

number = int(input())

print(maxDiffConseq(number))