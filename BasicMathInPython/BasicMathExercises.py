import math
radius = float(input("Insert the radius of a circle: "))

circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)

print(f"THe circumference of the circle is: {round(circumference, 2)}cm")
print(f"THe area of the circle is: {round(area, 2)}cm^2 \n")

print("Lets no calculate the hypothenuse of a triangle")
sideA = float(input("Insert side A: "))
sideB = float(input("Insert side B: "))

hypothenuse = math.sqrt((pow(sideA, 2)) + (pow(sideB,2)))

print(f"The hypothenuse of your triangle is: {math.round(hypothenuse, 2)}cm")