# n = int(input())
#
# for i in range(n):
#     print("* " * n)

count = int(input())

for i in range(count):
    print("*", end="")
    for j in range(count - 1):
        print(" *", end="")
    print()