n = int(input())
total = 0
number = 0
left_sum = 0
right_sum = 0

for j in range(1, n + 1):
    number = int(input())
    left_sum += number
for k in range(n + 1, n * 2 + 1):
    number = int(input())
    right_sum += number
total = abs(left_sum - right_sum)
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {total}")
