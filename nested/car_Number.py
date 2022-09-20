n = int(input())
m = int(input())

for a in range(n, m + 1):
    for b in range(n, m + 1):
        for c in range(n, m + 1):
            for d in range(n, m + 1):
                if a > d:
                    if (b + c) % 2 == 0:
                        if a % 2 == 0 and d % 2 != 0:
                            result = str(a) + str(b) + str(c) + str(d)
                            print(result, end=" ")
                        elif a % 2 != 0 and d % 2 == 0:
                            result = str(a) + str(b) + str(c) + str(d)
                            print(result, end=" ")