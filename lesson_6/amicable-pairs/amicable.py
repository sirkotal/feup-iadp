n = int(input("n:"))
m = int(input("m:"))

msum = 0
nsum = 0

for i in range(1, n):
    if (n % i == 0):
        nsum += i

for i in range(1, m):
    if (m % i == 0):
        msum += i

if (nsum == m) and (msum == n):
    print(str(n) + " and " + str(m) + " are friendly numbers")
else:
    print(str(n) + " and " + str(m) + " are not friendly numbers")