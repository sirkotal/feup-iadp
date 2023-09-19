n = int(input("n:"))
x = 0
pos = 0
neg = 0

while (x < n):
    z = int(input("value(" + str(x) + "):"))
    if z >= 0:
        pos += 1
    elif z < 0:
        neg += 1
    x += 1

print("% positive values = " + str(pos / n * 100) + "%")
print("% negative values = " + str(neg / n * 100) + "%")
