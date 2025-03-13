#Taylor Schmidt
#3/13/25
#P3HW2
#This program calculates an employee's salary based on hours worked and pay rate including overtime.

#Pseudocode:
#1. Display a message asking the user to enter the employee's name. (input)
#2. Display a message asking the user to enter the number of hours worked. (float)
#3. Display a message asking the user to enter the employee's pay rate. (float)
#4. Check if the number of hours worked is greater than 40:
   #- If TRUE (overtime):
     #a. Calculate overtime hours as: overtime_hours = hours_worked - 40
     #b. Set regular hours to 40 (maximum for regular pay).
     #c. Calculate overtime pay as: overtime_pay = overtime_hours * (pay_rate * 1.5)
 #If FALSE (no overtime):
     #a. Set regular hours to hours_worked (since all hours are regular).
#5 Calculate regular pay as: regular_pay = regular_hours * pay_rate
#6 Calculate gross pay as: gross_pay = regular_pay + overtime_pay
#Display these values in a table               
    #- Employee name
    #- Hours worked (formatted to 1 decimal place)
    #- Pay rate (formatted to 2 decimal places)
    #- Overtime hours (formatted to 1 decimal place)
    #- Overtime pay (formatted to 2 decimal places)
    #- Regular pay (formatted to 2 decimal places)
    #- Gross pay (formatted to 2 decimal places)


#User input

employee_name= input("Enter employee's name: ")
hours_worked= float(input("Enter numer of hours worked: "))
pay_rate= float(input("Enter employee's pay rate: "))

#Set over time hours, over time pay, and regular pay to zero

overtime_hours = 0
overtime_pay= 0
regular_pay= 0

# Determine regular and overtime pay

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40  # Max regular hours is 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    regular_hours = hours_worked  # All hours are regular if <= 40

# Calculate regular pay

regular_pay = regular_hours * pay_rate

# Calculate gross pay

gross_pay = regular_pay + overtime_pay

# Display results

print("-" * 40)
print(f"Employee name: {employee_name}")
print("-" * 40)
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print("-" * 90)
print(f"{hours_worked:<15.1f}${pay_rate:<15.2f}{overtime_hours:<15.1f}${overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<15.2f}")
