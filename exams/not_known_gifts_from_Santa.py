first = int(input())
last = int(input())
medium = int(input())

for i in range(last, first - 1, - 1):
    if i % 2 == 0 and i % 3 == 0:
        if i != medium:
            print(i, end=" ")
        else:
            break