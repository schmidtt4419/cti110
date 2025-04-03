#Taylor Schmidt
#3/27/25
#P4HW2
#Changing code to enable user to control loop

employees = []  # List to store employee data

total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

while True:
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    if employee_name == "Done":
        break
    
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    
    # Set over time hours, over time pay, and regular pay to zero
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = 0
    
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
    
    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    
    # Store employee details
    employees.append([employee_name, hours_worked, pay_rate, overtime_hours, overtime_pay, regular_pay, gross_pay])
    
    # Display individual employee results
    print(f"Employee name: {employee_name}")
    print()
    print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
    print("-" * 90)
    print(f"{hours_worked:<15.1f}${pay_rate:<15.2f}{overtime_hours:<15.1f}${overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<15.2f}")
    print()

# Display final summary
print()

print("Total number of employees entered:", len(employees))
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")