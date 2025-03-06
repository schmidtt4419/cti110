# Taylor Schmidt
# P3LAB
# 03/05/25
# Create a program that uses if statements to calculate the amount of money needed

# Get user input for the amount of money
amount = float(input("Enter the amount of money as a float: $"))

# Convert the amount to cents to avoid floating-point precision issues
amount_in_cents = int(round(amount * 100))

# Check if the amount is zero, meaning no change is needed
if amount_in_cents == 0:
    print("No change")
else:
    # Calculate the number of dollars
    dollars = amount_in_cents // 100  # Integer division to find whole dollars
    amount_in_cents -= dollars * 100  # Subtract the dollar value from the total cents
    if dollars > 0:
        print(dollars, "Dollar" if dollars == 1 else "Dollars")
        print("Remaining amount: $", amount_in_cents / 100)  # Display remaining amount
    
    # Calculate the number of quarters
    quarters = amount_in_cents // 25  # Find how many quarters fit in the remaining amount
    amount_in_cents -= quarters * 25  # Subtract the value of the quarters
    if quarters > 0:
        print(quarters, "Quarter" if quarters == 1 else "Quarters")
        print("Remaining amount: $", amount_in_cents / 100)
    
    # Calculate the number of dimes
    dimes = amount_in_cents // 10  # Find how many dimes fit in the remaining amount
    amount_in_cents -= dimes * 10  # Subtract the value of the dimes
    if dimes > 0:
        print(dimes, "Dime" if dimes == 1 else "Dimes")
        print("Remaining amount: $", amount_in_cents / 100)
    
    # Calculate the number of nickels
    nickels = amount_in_cents // 5  # Find how many nickels fit in the remaining amount
    amount_in_cents -= nickels * 5  # Subtract the value of the nickels
    if nickels > 0:
        print(nickels, "Nickel" if nickels == 1 else "Nickels")
        print("Remaining amount: $", amount_in_cents / 100)
    
    # Calculate the number of pennies
    pennies = amount_in_cents // 1  # Find how many pennies fit in the remaining amount
    if pennies > 0:
        print(pennies, "Penny" if pennies == 1 else "Pennies")
        print("Remaining amount: $", amount_in_cents / 100)