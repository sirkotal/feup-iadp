def average(l):
    total = 0
    for i in range(len(l)):
        total += l[i]
    result = total/len(l)
    return "{:.1f}".format(result)