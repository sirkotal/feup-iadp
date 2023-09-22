elem = int(input())

carbon = elem
lst = []
dct = {}

while (carbon > 0):
    num = int(input())
    lst.append(num)
    carbon -= 1

for i in range(len(lst)):
    if (lst[i] not in dct.keys()):
        dct[lst[i]] = 1
    else:
        dct[lst[i]] += 1

sdct = sorted(dct.items(), key = lambda x:x[1], reverse = True)

print("Number that appears most often =", "{:.2f}".format(int(sdct[0][0])))


for i in range(len(lst)):
    if (lst[i] == sdct[0][0]):
        print("Position:", i)
    else:
        continue
