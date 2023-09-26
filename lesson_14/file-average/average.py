def fileAverage(f, s):
    file1 = open(f, 'r')
    file2 = open(s, 'r')

    while True:
        line1 = file1.readline().strip()

        if (line1):
            value1 = int(line1)
        else:
            value1 = 0

        line2 = file2.readline().strip()

        if (line2):
            value2 = int(line2)
        else:
            value2 = 0

        if (not value1) and (not value2):
            break

        average = (value1 + value2) / 2
        print("{:.1f}".format(average))

    file1.close()
    file2.close()


f1 = input("Filename 1:")
f2 = input("Filename 2:")

fileAverage(f1, f2)