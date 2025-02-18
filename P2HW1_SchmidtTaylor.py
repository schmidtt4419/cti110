# Welcome to OpenREPL!

#Taylor Schmidt
#02/18/2025
#P2HW1
#Assignment assess student ability to edit and enhance exiting programs

#Print what this program does
print("This program calculates and displays travel expenses")

#Add blank line
print("")

#Ask user to enter their budget
budget = float(input("Enter Budget: "))

#Add blank line
print("")

#Ask user their destination
destination = (input("Enter Destination: "))

#Add blank line
print("")

#Ask user how much they will spend on gas
gas = float(input("How much do you think you will spend on gas? "))

#Add blank line
print("")

#Ask user how much they will spend on accomodation/hotel
accomodation = float(input("Approxiately, how much will you need for accomodation/hotel? "))

#Add blank line
print("")

#Ask user how much they will spend on food
food= float(input("Last, how much do you need for food? "))

#Add blank line
print("")

#Add expenses and subtract from the budget
result= budget - gas - accomodation - food

#Print the travel expenses in a formatted output using width formatting

#Print header
print("------------Travel Expenses------------")

#Print list
print(f"{"Location:":<25} {destination}")
print(f"{"Initial Budget:":<25} ${budget:,.2f}")
print(f"{"Fuel:":<25} ${gas:,.2f}")
print(f"{"Accommodation:":<25} ${accomodation:,.2f}")
print(f"{"Food:":<25} ${food:,.2f}")

#Print footer
print("--------------------------------------")

#Add blank line 
print("")

#Print remaining balnce
print(f"{"Remaining Balance:":<25} ${result}")