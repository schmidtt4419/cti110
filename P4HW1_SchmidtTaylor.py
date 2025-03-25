# Taylor Schmidt
# 3/25/25
# P4HW1
# Use nested loops to get valid grades from user

'''
Pseudocode

Create variable num_scores (int) -> user inpt number of scores
for each in range(num_scores)
    score=int(input(f"enter score # {each +1}))
    while score is invalid 
         score=int(input(Enter score # {each +1} again))
    Scores_list.append(score)
print scores_list to ensure correctness
'''
scores_list=[]

num_score=int(input("How many scores do you want to enter? "))
for each in range(num_score):
    score=int(input(f"Enter score #{each +1} "))
    if score <0 or score >100:
        print("INVALID Score entered!!!")
        print("Score shpuld be between 0 and 100")
        score=int(input(f"Enter score #{each +1} again: "))
    scores_list.append(score)


#Find the lowest grade
lowest_grade = min(scores_list)

#Find the sum of all grades
sum_of_grades = sum(scores_list)

#Find the average of all grades
avg= sum_of_grades / len(scores_list)


if avg >= 90:
   letter_grade = 'A'
elif avg >= 80:
    letter_grade = 'B'
elif avg >= 70:
    letter_grade = 'C'
elif avg >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print("-----------Results------------")
print(f"Lowest grade     : {lowest_grade}")
print(f"Modified list    : {scores_list}")
print(f"Score Average    : {avg:.2f}")
print(f"Grade            : {letter_grade}")
print("-------------------------------")

