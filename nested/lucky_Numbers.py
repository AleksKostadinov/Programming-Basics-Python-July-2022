n = int(input())

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                result = str(a) + str(b) + str(c) + str(d)
                if a + b == c + d:
                    if n % (a + b) == 0:
                        print(result, end=" ")