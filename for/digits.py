n = int(input())

a = n // 100
b = (n // 10) % 10
c = n % 10

for row in range(a + b):
    for col in range(a + c):
        if n % 5 == 0:
            n -= a
            print(n, end=" ")
        elif n % 3 == 0:
            n -= b
            print(n, end=" ")
        else:
            n += c
            print(n, end=" ")
    print()