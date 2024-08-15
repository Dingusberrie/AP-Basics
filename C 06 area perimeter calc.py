# Ask the user for the width and height
# (assume they put in valid data)
width = float(input("Width: "))
height = float(input("Height: "))

# calculate the area / perimeter
area = width * height
perimiter = 2 * (width * height)

# Output the area and perimeter
print()
print(f"Perimeter: {perimiter} units")
print(f"Area: {area} square units")