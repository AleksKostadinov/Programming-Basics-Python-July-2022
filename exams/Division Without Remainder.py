n = int(input())
count_p1 = 0
count_p2 = 0
count_p3 = 0
for i in range(1, n + 1):
    number = int(input())
    if number % 2 == 0:
        count_p1 += 1
    if number % 3 == 0:
        count_p2 += 1
    if number % 4 == 0:
        count_p3 += 1
p1 = (count_p1 / n) * 100
p2 = (count_p2 / n) * 100
p3 = (count_p3 / n) * 100
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
