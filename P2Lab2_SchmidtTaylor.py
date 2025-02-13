# Taylor Schmidt
# 2/13/25
# P2Lab2
# Assignment tests student's knowledge of how to write code that uses a dictionary to store user input and displays output to the user

# Create the dictionary with car models as keys and miles per gallon as values
vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Create a variable that holds all the keys in the dictionary using keys = my_dict.keys()
keys = vehicle_mpg.keys()

# Print the variable that holds the keys.
print("Available vehicles:", keys)

print("")

# Ask the user to enter a vehicle from above
vehicle = input("Enter a vehicle from above to see its MPG: ")

print("")

# Give the user the MPG for the vehicle they choose
mpg = vehicle_mpg[vehicle]
print(f"The {vehicle} gets {mpg} MPG.")

print("")

# Ask the user how many miles they will drive (f-string/ formatted string)
miles = float(input(f"How many miles will you drive the {vehicle}? "))

print("")

# Calculating fuel consumption
gallons_needed = miles / mpg

# Round fuel consumption
gallons_needed = round(gallons_needed,2)

# Display the result of how many gallons of gas are needed (f-string/ formatted string)
print(f"{gallons_needed} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")
