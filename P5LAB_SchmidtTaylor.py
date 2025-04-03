#Taylor Schmidt
#4/3/25
#P5LAB
#Write a program that simulate a customer using a self-checkout machine

#Import python random library
import random

def disperse_change(change):

    #Convert the float value into an integer
    change = int(change * 100)

    if change == 0:
        print("No Change Due")

    #Calculate the amount of each coin needed

    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickles = change // 5
    change = change - (num_nickles *5)

    num_pennies = change // 1

    #Display coins owed

    if num_dollars > 0:
        print(num_dollars,  end=" ")
        if num_dollars == 1:
            print("Dollar")
        else:
            print("Dollars")
            
    if num_quarters > 0:
        print(num_quarters,  end=" ")
        if num_quarters == 1:
            print("Quarter")
        else:
            print("Quarters")

    if num_dimes > 0:
        print(num_dimes,  end=" ")
        if num_dimes == 1:
            print("Dime")
        else:
            print("Dimes")

    if num_nickles > 0:
        print(num_nickles,  end=" ")
        if num_nickles == 1:
            print("Nickle")
        else:
            print("Nickles")

    if num_pennies > 0:
        print(num_pennies,  end=" ")
        if num_pennies == 1:
            print("Penny")
        else:
            print("Pennies")

def main():
    random_total=round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${random_total:.2f}")
    user_amount_paid=float(input("How much cash will you put in the self checkout? $"))
    change_owed=user_amount_paid-random_total
    print(f"Your change is: ${change_owed}")
    print()

    #Call the function disperse_change to show coins
    disperse_change(change_owed)

if __name__ == "__main__":
    main()

