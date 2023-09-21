n = int(input("n:"))
a = 0

up = 0
down = 0

while (a < n):
    x = int(input("X" + str(a) + ":"))
    p = int(input("P" + str(a) + ":"))
    up += x * p
    down += p
    a += 1

avg = up / down
print("Weighted average =", "{:.2f}".format(avg))