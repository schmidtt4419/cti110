# Taylor Schmidt
# 2/13/25
# P2Lab1
# Assignment tests student's knowledge of how to write code that performs mathematical calculations and displays information to users

# Circle Formulas
# Diameter = 2r
# Circumfrence = 2(pi)r
# Area=(pi)r^2

import math

# Ask the user for the radius
radius = float(input("What is the radius of your circle? "))

print("")

# Calculate the diameter
diameter = 2 * radius

# Round the diameter to one decimal place
diameter = round(diameter, 1)

# Output the diameter
print("The diameter of the circle is", diameter)

print("")

# Calculate the circumference
circumference = 2 * math.pi * radius

# Round the cirumference to two decimal places
circumference = round(circumference, 2)

# Output the circumference
print("The circumference of the circle is", circumference)

print("")

# Calculate the area
area = math.pi * (radius ** 2)

# Round the area to three decimal places
area = round(area, 3)

# Output the area
print("The area of the circle is", area)