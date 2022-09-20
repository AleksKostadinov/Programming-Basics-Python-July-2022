from math import ceil

x = int(input())
w = int(input())
m = int(input())

bricks_course = w * m
total_courses = ceil(x / bricks_course)
print(total_courses)
