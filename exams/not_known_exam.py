students = int(input())
weak_student = 0
good_student = 0
very_good_student = 0
excellent_student = 0
total_grades = 0
for student in range(students):
    grade = float(input())
    if grade <= 2.99:
        weak_student += 1
    elif grade <= 3.99:
        good_student += 1
    elif grade <= 4.99:
        very_good_student += 1
    else:
        excellent_student += 1
    total_grades += grade
percent_excellent_student = (excellent_student / students) * 100
percent_very_good_student = (very_good_student / students) * 100
percent_good_student = (good_student / students) * 100
percent_weak_student = (weak_student / students) * 100
avg_percent = total_grades / students
print(f"Top students: {percent_excellent_student:.2f}%")
print(f"Between 4.00 and 4.99: {percent_very_good_student:.2f}%")
print(f"Between 3.00 and 3.99: {percent_good_student:.2f}%")
print(f"Fail: {percent_weak_student:.2f}%")
print(f"Average: {avg_percent:.2f}")
