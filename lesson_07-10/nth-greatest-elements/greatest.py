elem = int(input("Number of elements in the list = "))

carbon = elem
lst = []

while (carbon > 0):
    num = int(input("l[" + str(elem-carbon) + "]="))
    lst.append(num)
    carbon -= 1

top = int(input("Number of greatest elements = "))

lst.sort(reverse=True)

print("[", end="")

for i in range(top):
    print(str(lst[i]), end="")
    if (i < top - 1):
        print(", ", end="")
    else:
        print("]")