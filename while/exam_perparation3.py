poor_grades = int(input())

sum_grades = 0
count_grades = 0
count_poor_grades = 0
last_problem = ""
input_line = input()
while input_line != "Enough":
    grade = int(input())
    if grade <= 4:
        count_poor_grades += 1

    if count_poor_grades == poor_grades:
        break

    count_grades += 1
    sum_grades += grade
    last_problem = input_line

    input_line = input()

if count_poor_grades == poor_grades:
    print(f"You need a break, {count_poor_grades} poor grades.")
else:
    avg_grade = sum_grades / count_grades
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_problem}")