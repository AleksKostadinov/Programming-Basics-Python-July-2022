number = input()
a = 0
b = 0
c = 0
result = 0
for a in range(1, int(number[2]) + 1):
    for b in range(1, int(number[1]) + 1):
        for c in range(1, int(number[0]) + 1):
            result = a * b * c
            print(f"{a} * {b} * {c} = {result};")
