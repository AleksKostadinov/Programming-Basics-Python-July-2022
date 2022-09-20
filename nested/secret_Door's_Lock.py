n_100 = int(input())
n_10 = int(input())
n_1 = int(input())

for i in range(1, n_100 + 1):
    for j in range(1, n_10 + 1):
        for k in range(1, n_1 + 1):
            if i % 2 == 0 and (j == 2 or j == 3 or j == 5 or j == 7) and k % 2 == 0:
                print(f"{i} {j} {k}")