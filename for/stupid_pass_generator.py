#https://judge.softuni.org/Contests/Practice/Index/1058#0
n = int(input())
l = int(input())
result = ""
for i1 in range(1, n + 1):
    for i2 in range(1, n + 1):
        for i3 in range(97, l + 97):
            for i4 in range(97, l + 97):
                for i5 in range(max(i1, i2) + 1, n + 1):
                    result += ("" + str(i1) + str(i2) + chr(i3) + chr(i4) + str(i5) + " ")
print(result.strip())