base = float(input("Base:"))
height = float(input("Height:"))

area = base * height / 2
result = "{:.2f}".format(area)
print("Area of the triangle =", str(result))
