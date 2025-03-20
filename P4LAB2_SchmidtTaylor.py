#Taylor Schmidt
#P4LAB2
#3/20/25
#Working with nested loops

# Write a variable to control the loops
run_again = "yes"

# While loop to control the main logic
while run_again.lower() != "no":
    integer = int(input("Enter an integer: "))
    if integer >=0: 
        for i in range (1,13):
            print(f"{integer} * {i} = {integer * i}")
    else:
        print("This program does not handle negative numbers.")
    

    run_again= input("Would you like to run the program again? ")
        
#While loop ends here
print("Program is ending! BYE!")
