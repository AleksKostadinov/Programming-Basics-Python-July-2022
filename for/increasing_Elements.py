#https://judge.softuni.org/Contests/Practice/Index/1059#7
n = int(input())
count = 0
next_num = 0
max_count = 0
for i in range(1, n + 1):
    a = int(input())
    if a > next_num:
        count += 1
    else:
        count = 1
    next_num = a

    if count > max_count:
        max_count = count
print(max_count)