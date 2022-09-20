#https://judge.softuni.org/Contests/Practice/Index/1059#8
n = int(input())

for i in range(1, n + 1):
    print((' ' * (n - i)) + '*', end='')

    for j in range(0, i - 1):
        print('-*', end='')

    print()
for i in reversed(range(1, n)):
    print(" " * (n - i) + '*', end='')

    for j in range(1, i):
        print('-*', end='')
    print()