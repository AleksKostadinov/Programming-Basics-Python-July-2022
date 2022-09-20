#https://judge.softuni.org/Contests/Practice/Index/1381#0
n1 = int(input())
n2 = int(input())
n3 = int(input())

for x1 in range(2, n1 + 1, 2):
    for x2 in range(2, n2 + 1):
        if x2 == 2 or x2 == 3 or x2 == 5 or x2 == 7:
            for x3 in range(2, n3 + 1, 2):
                print(f"{x1} {x2} {x3}")