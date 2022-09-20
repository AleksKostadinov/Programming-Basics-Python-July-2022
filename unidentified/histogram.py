n = int(input())
i, j, k, l, m = [0, 0, 0, 0, 0]
p1, p2, p3, p4, p5 = [0, 0, 0, 0, 0]
for h in range(1, n + 1):
    number = int(input())
    if number < 200:
        i += 1
        p1 = i / n * 100
    elif number <= 399:
        j += 1
        p2 = j / n * 100
    elif number <= 599:
        k += 1
        p3 = k / n * 100
    elif number <= 799:
        l += 1
        p4 = l / n * 100
    else:
        m += 1
        p5 = m / n * 100

print(f"{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%\n{p4:.2f}%\n{p5:.2f}%")
