import sys
n = int(input())
max_num = -sys.maxsize
summ = 0

for i in range(1, n + 1):
    number = int(input())

    if number > max_num:
        max_num = number

    summ += number

if max_num == summ - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    summ = summ - max_num
    print(f"Diff = {abs(max_num - summ)}")