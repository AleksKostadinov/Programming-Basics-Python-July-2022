num = int(input())
total = 0

while True:
    total += num % 10
    num //= 10
    if not num > 0:
        break
print(total)
