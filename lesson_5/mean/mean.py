n = int(input("n:"))
x = 0

total = 0

while (x < n):
    z = int(input("value(" + str(x+1) + "):"))
    total += z
    x += 1

result = total / x
print("Arithmetic mean =", "{:.2f}".format(result))