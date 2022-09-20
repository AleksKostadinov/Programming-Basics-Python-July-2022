bad_grades = int(input())

name_problem = ""
count = 0
grades = 0
total = 0
good_grades_count = 0
bad_grades_count = 0
last_problem = ""
while name_problem != "Enough":
    count = good_grades_count + bad_grades_count
    last_problem = name_problem
    name_problem = input()

    if name_problem == "Enough":
        avg = total / count
        print(f"Average score: {avg:.2f}")
        print(f"Number of problems: {count}")
        print(f"Last problem: {last_problem}")
        break
    grades = int(input())

    if grades <= 4:
        total += grades
        bad_grades_count += 1
        if bad_grades_count == bad_grades:
            print(f"You need a break, {bad_grades_count} poor grades.")
            break
    elif grades > 4:
        good_grades_count += 1
        total += grades