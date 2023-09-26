def fileRead(f, s):
    file1 = open(f, 'r')
    file2 = open(s, 'r')

    while True:
        line1 = file1.readline()

        content1 = line1.split()

        for something in (content1):
            print(something)

        if (not line1):
            break

    while True:
        line2 = file2.readline()

        content2 = line2.split()

        for something in (content2):
            print(something)

        if (not line2):
            break

    file1.close()
    file2.close()


f1 = input("Filename 1:")
f2 = input("Filename 2:")

fileRead(f1, f2)