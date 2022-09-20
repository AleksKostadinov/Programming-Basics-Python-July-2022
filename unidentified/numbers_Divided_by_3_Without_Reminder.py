n = int(input())
summ = 0
for i in range(1, n + 1):
    number = int(input())
    summ += number
    i += 1
print(f"{summ / n:.2f}")