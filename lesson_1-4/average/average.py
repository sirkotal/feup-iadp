n = int(input("n:"))
x = 0

lst = []
total = 0

while (x < n):
    z = int(input("value(" + str(x) + "):"))
    lst.append(z)
    x += 1

lst.sort()

del lst[0]
del lst[x-1-1]

for num in lst:
    total += num

result = total / len(lst)
print("Average =", "{:.2f}".format(result))
