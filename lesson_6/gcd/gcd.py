x = int(input("value 1:"))
y = int(input("value 2:"))

gcd = 0

for i in range(1, x + y):
    if (x % i == 0) and (y % i == 0):
        gcd = i

print("the greatest common factor of " + str(x) + " and " + str(y) + " is", gcd)