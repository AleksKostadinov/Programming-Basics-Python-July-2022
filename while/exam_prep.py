failed = int(input())
bad_grades = 0
good_grades = 0
grades_sum = 0
last_problem = ""
has_failed = True

while bad_grades < failed:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break

    grade = int(input())
    if grade <= 4:
        bad_grades += 1
    grades_sum += grade
    good_grades += 1
    last_problem = problem_name

if has_failed:
    print(f"You need a break, {failed} poor grades.")
else:
    print(f"Average score: {grades_sum / good_grades:.2f}")
    print(f"Number of problems: {good_grades}")
    print(f"Last problem: {last_problem}")