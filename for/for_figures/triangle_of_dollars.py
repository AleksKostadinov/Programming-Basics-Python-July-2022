# n = int(input())
#
# for i in range(1, n + 1):
#     print("$ " * i)

count = int(input())

for i in range(count):
    print("$", end="")
    for j in range(i):
        print(" $", end="")
    print()