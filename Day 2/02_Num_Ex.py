import math
radius = float(input("Type the Radius of Circle : "))

Area = math.pi * radius**2
circumference = 2 * math.pi * radius

print("Area of Circle:",round(Area,2))
print("Circumference of Circle:",round(circumference,2))
