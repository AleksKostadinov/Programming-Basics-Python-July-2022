#https://judge.softuni.org/Contests/Practice/Index/1059#10
a = int(input())
b = int(input())
count = 0

for i in range(a, b + 1):
    for j in range(i + 1, b + 1):
        for k in range(j + 1, b + 1):
            for l in range(k + 1, b + 1):
                print('%d %d %d %d' % (i, j, k, l))
                count += 1
if count == 0:
    print("No")
