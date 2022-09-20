men = int(input())
women = int(input())
tables = int(input())
count = 0
for i in range(1, men + 1):
    for j in range(1, women + 1):
        if count < tables:
            result = f"({i} <-> {j})"
            count += 1
            print(result, end=" ")