a = int(input())
b = int(input())
result = ""
for i in range(1, a + 1):
    for j in range(1, a + 1):
        for k in range(97, 97 + b):
            for l in range(97, 97 + b):
                for m in range(1, a + 1):
                    if m > i and m > j:
                        result = str(i) + str(j) + chr(k) + chr(l) + str(m)
                        print(result, end=" ")