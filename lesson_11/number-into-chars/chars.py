def numIntoChar(num):
    strnum = str(num)
    counter = len(strnum)

    print("Number of digits =", counter)

    for i in range(counter):
        print("Pos number " + str(i) + " =", strnum[i])


number = input()

numIntoChar(number)