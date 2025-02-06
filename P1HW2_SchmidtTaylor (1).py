# Welcome to OpenREPL!

#Taylor Schmidt
#02/06/2025
#P1HW2
#Create a program that does some basic math on numbers that are entered

#Ask user to enter their budget
budget = int(input("Enter Budget: "))

#Ask user their destination
destination = (input("Enter Destination: "))

#Ask user how much they will spend on gas
gas = int(input("How much do you think you will spend on gas? "))

#Ask user how much they will spend on accomodation/hotel
accomodation = int(input("Approxiately, how much will you need for accomodation/hotel? "))

#Ask user how much they will spend on food
food= int(input("Last, how much do you need for food? "))

#Add expenses and subtract from the budget
result= budget - gas - accomodation - food

#Add blank line
print("")

#Display expenses and leftover budget

#Print destination and initial budget
print("------------Travel Expenses------------")
print("Location: ", destination)
print("Initial Budget: ", budget)

#Add blank line
print("")

#Print expenses
print("Fuel: ", gas)
print("Accomodation: ", accomodation)
print("Food: ", food)

#Add blank line 
print("")

#Print remaining balnce
print("Remaining Balance: ", result)