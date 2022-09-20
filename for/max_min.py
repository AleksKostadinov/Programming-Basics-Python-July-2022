n = int(input())
summ_even = 0
summ_odd = 0
summ = 0

for i in range(1, n + 1):
    numbers = int(input())

    if i % 2 == 0:
        summ_even += numbers
    else:
        summ_odd += numbers

summ = abs(summ_even - summ_odd)

if summ_even == summ_odd:
    print(f"Yes")
    print(f"Sum = {summ_even}")
else:
    print(f"No")
    print(f"Diff = {summ}")
