#https://judge.softuni.org/Contests/Practice/Index/1059#6
n = int(input())
sum1 = 0
sum2 = 0
sum3 = 0

for i in range(0, n):
    a = int(input())
    if i % 3 == 0:
        sum1 += a
    elif i % 3 == 1:
        sum2 += a
    elif i % 3 == 2:
        sum3 += a
print(f"sum1 = {sum1}")
print(f"sum2 = {sum2}")
print(f"sum3 = {sum3}")