n = int(input())
sum_even = 0
sum_odd = 0
summ = 0

for i in range(1, n + 1):
    numbers = int(input())

    if i % 2 == 0:
        sum_even += numbers
    else:
        sum_odd += numbers

summ = abs(sum_even - sum_odd)

if sum_even == sum_odd:
    print(f"Yes")
    print(f"Sum = {sum_even}")
else:
    print(f"No")
    print(f"Diff = {summ}")
