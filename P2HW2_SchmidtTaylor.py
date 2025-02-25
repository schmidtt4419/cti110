#Taylor Schmidt
#2/25/25
#P2HW2
#For assignment this assignment, you are to design a program that does the following: ask the user to enter grades for Modules 1-6, store grades entered in a list, and display the lowest grade.. highest garde.. sum of grades.. and grade average

#Input grades from the user and put them into this list
module_grades = []

#Ask the user to input grades for each module (W3 Schools Loop Lists)
#i represets index... has to be 1-7 because python assigns the first input as 0...
#append modifies the original list directly by adding the new element as its last item... 

for i in range(1, 7): 
    grade = float(input(f"Enter the grade for Module {i}: "))
    module_grades.append(grade)

#Calculations to find min, max, sum, and average

#Find the lowest grade
lowest_grade = min(module_grades)  

#Find the highest grade
highest_grade = max(module_grades)

#Find the sum of all grades
sum_of_grades = sum(module_grades)

#Find the average of all grades
#len() is a built-in function in Python that returns the number of items in an object.. AKA 6 for this assignment because there are 6 modules
average_grade = sum_of_grades / len(module_grades)

#Blank space
print()

#Display the results
print("-----------Results------------")
print(f"Lowest grade: {lowest_grade}")
print(f"Highest grade: {highest_grade}")
print(f"Sum of grades: {sum_of_grades}")
print(f"Average grade: {average_grade:.2f}")
print("---------------------------------------")