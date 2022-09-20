#https://judge.softuni.bg/Contests/Practice/Index/1059#3
x = int(input())
y = int(input())

point_in_rect1 = 2 <= x <= 12 and -3 <= y <= 1
point_in_rect2 = 4 <= x <= 10 and -5 <= y <= 3

if point_in_rect1 or point_in_rect2:
    print("in")
else:
    print("out")