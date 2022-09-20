# https://judge.softuni.org/Contests/Practice/Index/1060#3
num_students = int(input())
a_students = 0
b_students = 0
c_students = 0
d_students = 0
total_grades = 0

for i in range(1, num_students + 1):
    grades = float(input())
    total_grades += grades

    if grades <= 2.99:
        d_students += 1
    elif 3.00 <= grades <= 3.99:
        c_students += 1
    elif 4.00 <= grades <= 4.99:
        b_students += 1
    else:
        a_students += 1

a_grades = a_students / num_students * 100
b_grades = b_students / num_students * 100
c_grades = c_students / num_students * 100
d_grades = d_students / num_students * 100
average_grade = total_grades / num_students

print(f"Top students: {a_grades:.2f}%")
print(f"Between 4.00 and 4.99: {b_grades:.2f}%")
print(f"Between 3.00 and 3.99: {c_grades:.2f}%")
print(f"Fail: {d_grades:.2f}%")
print(f"Average: {average_grade:.2f}")
